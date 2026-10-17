# Captions.ai caption-style research

Reference material for building animated caption templates (Premiere Pro / After Effects) from Captions.ai's public AI Edit Styles.

| File | What it is |
|---|---|
| `ai-edit-styles.json` | Full catalog pulled from `GET https://internal.captions-api.com/studio-go/ai-edit-styles` (152 styles: names, tags, aspect ratios, colour presets, preview and thumbnail URLs). |
| `ai-edit-styles.md` | Same catalog as a readable table. |
| `caption-motion-patterns.md` | Per-style motion specs for 21 representative styles plus a cross-style summary of 7 recurring patterns with timing (ms), easing and placement (%) parameters, and a suggested MOGRT parameter set. |
| `previews/` | Preview mp4s are not committed (about 450 MB). Re-download with the script below. |

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
PY
```

Captions.ai content is theirs; this is a study of publicly served previews for building original templates.
