# Captions.ai caption-style research

Reference material for building animated caption templates (Premiere Pro / After Effects) from Captions.ai's public AI Edit Styles.

| File | What it is |
|---|---|
| `ai-edit-styles.json` | Full catalog pulled from `GET https://internal.captions-api.com/studio-go/ai-edit-styles` (152 styles: names, tags, aspect ratios, colour presets, preview and thumbnail URLs). |
| `ai-edit-styles.md` | Same catalog as a readable table. |
| `caption-motion-patterns.md` | Per-style motion specs for all 54 premium styles (21 in detail, 33 compact), a cross-style summary of recurring patterns with timing (ms), easing and placement (%) parameters, the basic-preset colour-slot mapping, and measured placement/hold/entrance statistics. |
| `caption-styles.json` / `.md` | The 67 basic caption presets from `GET .../studio-go/caption-styles` with their 4-slot colour arrays and preview URLs. |
| `measurements.csv` | Machine-measured caption band position, chunk hold, entrance duration and accent colours for 129 previews. |
| `tools/measure_captions.py` | The measurement script (numpy + ffmpeg). |
| `previews/` | Preview mp4s are not committed (about 1.2 GB for all premium styles plus `previews/caption-styles/` for the basic presets). Re-download with the script below. |

## Re-download the previews

```bash
mkdir -p previews && python3 - <<'PY'
import json, re, subprocess
for s in json.load(open('ai-edit-styles.json')):
    for key, ori in (('vertical','9x16'),('horizontal','16x9')):
        p = s['previews'].get(key)
        if not p: continue
        fn = re.sub(r'[^a-z0-9]+','-', s['name'].lower()).strip('-') + f'-{ori}.mp4'
        subprocess.run(['curl','-sSL','-o',f'previews/{fn}', p['previewVideoUrl']])
import os; os.makedirs('previews/caption-styles', exist_ok=True)
for s in json.load(open('caption-styles.json')):
    fn = re.sub(r'[^a-z0-9]+','-', s['name'].lower()).strip('-') + '.mp4'
    subprocess.run(['curl','-sSL','-o',f'previews/caption-styles/{fn}', s['previewVideoUrl']])
PY
```

Captions.ai content is theirs; this is a study of publicly served previews for building original templates.
