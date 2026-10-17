"""Measure caption motion from a preview video, no model needed.

For every preview this reports, per frame at native fps:
  * where the caption band is (text-pixel centroid y as % of height),
  * when chunks change (big jumps in the band's pixel content),
  * how long each chunk's entrance lasts (frames until the band stops changing),
  * dominant non-grey colours inside the band (accent colours).

usage: python3 -I measure_captions.py previews/*.mp4 --out measurements.csv [--json measurements.json]

ponytail: text is found as "bright, high-contrast, sharp" pixels in the lower 60% of frame
(or the whole frame for 16:9 flat previews); that is good enough to find a caption band in
these previews but will miss dark-on-light captions. Flagged as band_conf < 0.3.
"""
import argparse, csv, json, os, subprocess, sys
import numpy as np

def probe(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,nb_frames", "-show_entries", "format=duration",
        "-of", "json", path])
    j = json.loads(out); s = j["streams"][0]
    num, den = s["r_frame_rate"].split("/"); fps = float(num) / float(den)
    return int(s["width"]), int(s["height"]), fps, float(j["format"]["duration"])

def frames(path, w, h, scale_w=360):
    """Yield (gray uint8 HxW, rgb uint8 HxWx3) frames scaled to scale_w wide."""
    sh = int(round(h * scale_w / w / 2)) * 2
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-vf", f"scale={scale_w}:{sh}",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    n = scale_w * sh * 3
    while True:
        buf = p.stdout.read(n)
        if len(buf) < n: break
        rgb = np.frombuffer(buf, np.uint8).reshape(sh, scale_w, 3)
        yield rgb
    p.stdout.close(); p.wait()

def text_mask(rgb):
    """Pixels that look like rendered text: bright OR saturated, with strong local contrast."""
    f = rgb.astype(np.int32)
    lum = (f[..., 0] * 299 + f[..., 1] * 587 + f[..., 2] * 114) // 1000
    sat = f.max(-1) - f.min(-1)
    # local contrast: difference to a 5px box blur (cheap, via cumulative sums)
    k = 7
    pad = np.pad(lum, 3, mode="edge").astype(np.int32)
    c = np.pad(pad.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    box = (c[k:, k:] - c[:-k, k:] - c[k:, :-k] + c[:-k, :-k]) // (k * k)
    contrast = np.abs(lum - box)
    return ((lum > 170) | (sat > 120)) & (contrast > 40)

def analyse(path, sample_every=1):
    w, h, fps, dur = probe(path)
    portrait = h > w
    rows = []          # per-frame: (i, band_y, band_count)
    band_imgs = []     # per-frame band crop (small) for change detection
    masks = []
    for i, rgb in enumerate(frames(path, w, h)):
        m = text_mask(rgb)
        H = m.shape[0]
        # candidate region: lower 60% for portrait, whole frame otherwise
        y0 = int(H * 0.4) if portrait else 0
        sub = m[y0:]
        ys = np.nonzero(sub)[0]
        if len(ys) > 40:
            # dominant horizontal band: histogram of rows, pick densest 12%-high window
            hist = sub.sum(1).astype(float)
            win = max(4, int(H * 0.12))
            cs = np.concatenate([[0], hist.cumsum()])
            dens = cs[win:] - cs[:-win]
            j = int(dens.argmax())
            band_y = (y0 + j + win / 2) / H
            count = int(dens[j])
            crop = m[y0 + j: y0 + j + win]
            cimg = rgb[y0 + j: y0 + j + win]
        else:
            band_y, count, crop, cimg = float("nan"), 0, None, None
        rows.append((i, band_y, count))
        masks.append(crop); band_imgs.append(cimg)

    n = len(rows)
    counts = np.array([r[2] for r in rows], float)
    ys = np.array([r[1] for r in rows], float)
    # per-frame band change (xor / union) and global frame change (scene cuts, B-roll motion)
    change = np.zeros(n); iou = np.ones(n)
    for i in range(1, n):
        a, b = masks[i - 1], masks[i]
        if a is None or b is None or a.shape != b.shape:
            change[i] = 1.0 if (a is None) != (b is None) else 0.0; iou[i] = 0.0
        else:
            u = (a | b).sum(); x = (a & b).sum()
            change[i] = ((a ^ b).sum() / u) if u else 0.0
            iou[i] = (x / u) if u else 1.0
    gdiff = np.zeros(n)
    for i in range(1, n):
        if band_imgs[i] is None or band_imgs[i - 1] is None or band_imgs[i].shape != band_imgs[i - 1].shape: continue
        gdiff[i] = np.abs(band_imgs[i].astype(int) - band_imgs[i - 1].astype(int)).mean()
    scene_cut = gdiff > 28  # the footage behind the band changed a lot: ignore as a caption event
    # chunk boundary: most of the previous text is gone (IoU < 0.25) and text is present now
    # word event: text present before and after, overlap kept (IoU 0.25-0.92) and mask grew or recoloured
    raw_chunks = [i for i in range(1, n) if counts[i] > 0 and iou[i] < 0.25 and not scene_cut[i]]
    raw_words = [i for i in range(1, n) if counts[i] > 0 and counts[i - 1] > 0 and 0.5 <= iou[i] < 0.9 and counts[i] > counts[i - 1] * 1.2 and not scene_cut[i]]
    def merge(ev, gap):
        out = []
        for b in ev:
            if out and b - out[-1] < gap: continue
            out.append(b)
        return out
    merged = merge(raw_chunks, int(fps * 0.25))
    words = merge([w for w in raw_words if all(abs(w - c) >= int(fps * 0.2) for c in merged)], int(fps * 0.12))
    entrances = []
    for b in merged:
        k = b
        while k + 1 < n and change[k + 1] > 0.06 and k + 1 - b < int(fps * 0.5): k += 1
        entrances.append(k - b + 1)
    hold = np.diff(merged) / fps if len(merged) > 1 else np.array([])
    text_frames = max(1, int((counts > 0).sum()))
    words_per_s = len(words) / (text_frames / fps)

    # accent colours: saturated pixels inside the band, quantised
    acc = {}
    for cimg, m in zip(band_imgs, masks):
        if cimg is None: continue
        px = cimg[m]
        if not len(px): continue
        f = px.astype(int); sat = f.max(1) - f.min(1)
        sel = px[sat > 90]
        if not len(sel): continue
        q = (sel // 32) * 32 + 16
        for c in map(tuple, q[:: max(1, len(q) // 400)]):
            acc[c] = acc.get(c, 0) + 1
    top = sorted(acc.items(), key=lambda kv: -kv[1])[:3]
    tot = sum(acc.values()) or 1
    accents = ["#%02x%02x%02x" % c for c, v in top if v / tot > 0.08]

    valid = ~np.isnan(ys)
    conf = float(valid.mean())
    return dict(
        file=os.path.basename(path), w=w, h=h, fps=round(fps, 2), dur_s=round(dur, 2),
        band_conf=round(conf, 2),
        band_y_pct=round(float(np.nanmedian(ys)) * 100, 1) if valid.any() else None,
        band_y_iqr_pct=round(float(np.nanpercentile(ys, 75) - np.nanpercentile(ys, 25)) * 100, 1) if valid.any() else None,
        chunks=len(merged),
        word_events=len(words),
        word_events_per_s=round(words_per_s, 2),
        reveal=('word' if len(words) >= 0.8 * max(1, len(merged)) else 'chunk'),
        chunk_hold_med_s=round(float(np.median(hold)), 2) if len(hold) else None,
        chunk_hold_min_s=round(float(hold.min()), 2) if len(hold) else None,
        entrance_med_frames=int(np.median(entrances)) if entrances else None,
        entrance_med_ms=int(round(np.median(entrances) / fps * 1000)) if entrances else None,
        entrance_p90_ms=int(round(np.percentile(entrances, 90) / fps * 1000)) if entrances else None,
        accents=" ".join(accents),
    )

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("videos", nargs="+")
    ap.add_argument("--out", default="measurements.csv")
    ap.add_argument("--json")
    a = ap.parse_args()
    res = []
    for v in a.videos:
        try:
            r = analyse(v); res.append(r)
            print(f"{r['file']:40s} y={r['band_y_pct']} conf={r['band_conf']} chunks={r['chunks']} words={r['word_events']} reveal={r['reveal']} "
                  f"hold={r['chunk_hold_med_s']}s entrance={r['entrance_med_ms']}ms acc={r['accents']}", flush=True)
        except Exception as e:
            print(f"{v}: FAILED {e}", file=sys.stderr)
    keys = list(res[0].keys())
    with open(a.out, "w", newline="") as f:
        wr = csv.DictWriter(f, keys); wr.writeheader(); wr.writerows(res)
    if a.json: json.dump(res, open(a.json, "w"), indent=1)

if __name__ == "__main__":
    main()
