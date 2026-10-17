# Captions.ai caption-motion patterns

Observed from the public AI Edit Style preview videos (source list: `ai-edit-styles.json`).
Previews downloaded to `previews/` (21 styles, 23 files; the two "basic" styles have both orientations).
Frames were extracted at 10 fps and studied as contact sheets, with native-fps (24–30 fps) zoom strips on the caption band for entrance timing.

Conventions used below

- Positions are % of frame height from the top (y) and % of frame width from the left (x). 9:16 = 1080×1920, 16:9 = 1920×1080.
- Timing is in ms, rounded to the nearest frame of the source clip (24, 25 or 30 fps). Values under 50 ms mean "cuts on, no visible transition".
- "Chunk" = the caption group shown at once (1–4 words). Captions.ai never shows full sentences; chunks are 1–3 s long, cut on speech.
- "Highlight word" = the word (usually the stressed/keyword) rendered in the accent colour or heavier weight while the rest of the chunk stays neutral.
- Easing names follow After Effects / CSS vocabulary: `linear`, `easeOut` (cubic ~ (0.2, 0.8, 0.2, 1)), `easeOutBack` (overshoot ~ 1.15), `easeInOut`.

---

## Part 1 — Per-style specs

### 1. Prism Pro · 9:16 · Business, New

| Attribute | Observed |
|---|---|
| Placement | **Top of frame.** Two-line stack anchored top-left, y ≈ 3–12 %, x ≈ 4–8 %. Nothing in the lower third. |
| Font | Grotesk sans (Inter/Helvetica-like). Line 1 regular weight, white, sentence case. Line 2 the keyword in **bold italic**, ~1.6× the size of line 1. |
| Reveal | Word-by-word on line 1 (each word fades in over ~80 ms, no motion). Keyword drops in as a full word. |
| Highlight | Keyword rendered larger, bold-italic, with a soft gold→white gradient fill ("Mistake", "Focusing", "Only"). No colour change on plain words. |
| Entrance / exit | Keyword: opacity 0→1 + ~4 % scale-down over ~125 ms `easeOut`. Chunk exit: hard cut when the next chunk starts; no exit animation. |
| Box / stroke / shadow | None. Text sits directly on footage; subtle 10–15 % drop shadow only. |
| Accents | Radial / zoom blur punch-in on the speaker at chunk boundaries (~250 ms), whole-frame defocus wipe between scenes. No emoji. |

### 2. Paper II · 9:16 · Trending, Polished, Educational, Lifestyle

| Attribute | Observed |
|---|---|
| Placement | Centre-bottom pill, y ≈ 75 %, centred. |
| Font | Rounded geometric sans (Poppins-like), ~44 px cap height, sentence case. |
| Reveal | **Word fill.** The whole chunk is laid out at once in light grey (~45 % white); each spoken word turns solid dark as it is said. Layout never reflows. |
| Highlight | Spoken-word colour only (grey → near-black). No scale. |
| Entrance | Pill + text: opacity 0→1 with ~2 px blur→0 over ~80 ms (2 frames @25 fps). Exit: cut. |
| Box | Off-white pill (≈ #F2F2F2 at 92 % opacity), radius ≈ 50 % of height, padding ≈ 0.5em horizontally, 0.3em vertically. Soft shadow 8 px / 20 %. |
| Accents | Torn-paper collage title card at the top (y ≈ 5–20 %) with typewriter-label stickers ("PRESENCE / WITHOUT PRESSURE") that type on letter-by-letter (~40 ms/char). Cut-out B-roll stickers (cup, clock, typewriter) scale in with `easeOutBack` over ~300 ms, staggered ~100 ms. |

### 3. Prime · 9:16 · Trending, Minimal, Business

| Attribute | Observed |
|---|---|
| Placement | Centre, y ≈ 74 %. One or two short lines. |
| Font | Heavy geometric sans (Inter Black / Satoshi Bold), ~48 px, sentence case, white. |
| Reveal | **Word fill with soft fade.** Chunk laid out in advance; each word fades from ~35 % to 100 % white over ~100 ms (2–3 frames @24 fps). |
| Highlight | None by colour; emphasis comes from occasional single-word chunks. |
| Entrance | First word of chunk fades in (~100 ms). Exit: cut. |
| Box / stroke / shadow | No box. 1 px dark stroke + 6 px shadow at ~40 %. |
| Accents | Neon rectangle outline (≈ #6EF2E8, 3 px) drawn on around the speaker, with a script-font keyword ("Progress") written above it in the same neon; outline and script glow (outer glow 12 px). Zoom punch-in ~6 % at some chunk starts. B-roll inserts framed by the same neon rectangle. |

### 4. Elevate · 9:16 · Trending, Minimal, Lifestyle

| Attribute | Observed |
|---|---|
| Placement | Centre, y ≈ 70 %. Thin hairline rule at y ≈ 95 %, tiny meta text ("creator", "short film") at y ≈ 3 %. |
| Font | Light serif (Playfair / Times-like) ~40 px, white, sentence case. Emphasised words switch to **italic** of the same face. |
| Reveal | Whole chunk appears at once (no word-by-word). |
| Highlight | Italic for keywords ("my 20-year-old", "self"). No colour. |
| Entrance | Opacity 0→1 over ~120 ms with a slight blur-out (4 px→0). Exit: fade ~80 ms. |
| Box / stroke / shadow | None. Very light shadow. |
| Accents | Script-font title ("Momentum") with a small oval-badge subtitle and ✶ ornament at y ≈ 45 %; it fades in over ~300 ms and later blurs out. B-roll panel slides up from the bottom edge over ~400 ms `easeOut` and the caption re-anchors onto it. |

### 5. Impact II · 9:16 · Trending, Bold, Business

| Attribute | Observed |
|---|---|
| Placement | Centre, y ≈ 70 %. Single line. |
| Font | Condensed bold sans (Bebas / Oswald), ALL CAPS, ~56 px; single-word chunks jump to ~90 px. |
| Reveal | **Whole chunk pops.** No word-by-word. |
| Highlight | Alternating colour per chunk: cyan (≈ #35D0FF) for ordinary chunks, white for the single-word emphasis chunk ("BALANCE"). |
| Entrance | Scale 1.15→1.0 + blur 6 px→0 + opacity 0→1 over ~125 ms (3 frames @24 fps), `easeOut`. Exit: cut. |
| Box / stroke / shadow | No box. Dark 2 px stroke + 8 px drop shadow. Chromatic-aberration fringe on the first frame. |
| Accents | Whole-frame glitch/RGB-split transition (~200 ms) at scene changes; zoom punch-in on emphasis words; B-roll slides in from the right with the same glitch. |

### 6. Pop · 9:16 · New, Lifestyle, Entertainment, Bold, Trending

| Attribute | Observed |
|---|---|
| Placement | Small pill, centre, y ≈ 78 %. |
| Font | Rounded sans (Quicksand / Nunito) ~34 px, **lower case**, black on white. Keywords in bold, the rest in italic regular. |
| Reveal | Whole chunk at once. |
| Highlight | Bold weight on the keyword ("jacket cost", "best"). |
| Entrance | Pill scales 0.8→1.0 with `easeOutBack` over ~150 ms. Exit: cut. |
| Box | White pill with 2 px black outline, radius full. |
| Accents | Sticker storm: flat pink/green/yellow shapes (stars, lightning, arrows, bursts) with 3 px black outline and 4 px offset black shadow. Each sticker scales in `easeOutBack` over ~200 ms, staggered 60–100 ms. Title banner ("PROJECT") is a pink box that **wipes open horizontally** from a 1-px line over ~200 ms, then text types on. Pastel checkerboard / grid backgrounds behind B-roll; B-roll shown as tilted photo stack. |

### 7. Y2K · 9:16 · New, Trending, Bold, Entertainment

| Attribute | Observed |
|---|---|
| Placement | Floats with the collage; caption chunk at y ≈ 20–35 %, left-aligned to the visual. |
| Font | Thin sans (Helvetica Light), **neon yellow** (≈ #E6FF00), sentence case, ~36 px, two short lines. |
| Reveal | Word-by-word append, instant (no fade). |
| Highlight | No per-word highlight; a script "Summer" title in the same yellow sits over the collage. |
| Entrance | Instant. Exit: cut. |
| Box / stroke / shadow | None. |
| Accents | Pale-yellow paper background; speaker video mapped inside a cluster of early-2000s phone screens that tumble in from the top (`easeOut`, ~600 ms, rotation ±15°). Later a macOS-style window stack slides in from the right (3 copies, 12 px offset). Rapid zoom to a single phone, then hard cuts. |

### 8. Form · 9:16 · New, Trending, Bold, Motivation

| Attribute | Observed |
|---|---|
| Placement | Centre, y ≈ 72 %. |
| Font | Grotesk sans. Regular words ~40 px white; keyword in **bold italic** at ~1.3× ("what's **up**", "**motivation** is"). |
| Reveal | Whole chunk at once. |
| Highlight | Weight + italic + size on the keyword; no colour change. |
| Entrance | Opacity 0→1 + 3 px blur→0 over ~80 ms. Exit: cut. |
| Box / stroke / shadow | None. Light shadow. |
| Accents | Full-bleed orange (≈ #E8502A) panels with diagonal cut edges that slide across the frame (~250 ms `easeInOut`); a huge yellow (≈ #FFF24A) italic title ("RESULTS") that **types off** letter by letter from the right (~40 ms per character) as the panel exits. Thin orange vertical "scan" bars overlay the footage during the body. |

### 9. Chalk · 9:16 · New, Educational

| Attribute | Observed |
|---|---|
| Placement | Caption at y ≈ 73 %, two short lines; title word at y ≈ 5–15 %. |
| Font | Handwritten marker (Caveat / Patrick Hand style) ~38 px, white; keywords in **yellow** (≈ #FFD400) at ~1.4× size. |
| Reveal | Word-by-word; each word fades in ~80 ms. Keywords additionally pop 1.1→1.0. |
| Highlight | Yellow colour + size. |
| Entrance | Word fade. Exit: cut. |
| Box | Dark pill (≈ #222 at 85 %) behind each **line**, radius ≈ 8 px, padding 0.4em. The pill grows to fit as words append. |
| Accents | Chalkboard texture backgrounds. Hand-drawn **draw-on** title ("YOUTH") that writes itself over ~200 ms (5 frames @24 fps) with a doubled ghost line underneath. Yellow scribble outline traced around the speaker. Yellow squiggle lines and torn-edge photo cut-outs that slide in; B-roll cut-outs have a wobbly yellow marker border. |

### 10. Ember · 9:16 · Trending, Motivation, Entertainment

| Attribute | Observed |
|---|---|
| Placement | Centre, y ≈ 70 %. Single short line (1–2 words). |
| Font | Grotesk sans ~46 px, warm cream (≈ #F2E6C8), sentence case, regular weight. |
| Reveal | Whole chunk at once, 1–2 words per chunk (fast cadence, ~400–700 ms per chunk). |
| Highlight | Separate **red keyword title** (≈ #E8403A, 60–70 % opacity, all caps, ~40 px) parked at y ≈ 50 % for several chunks ("LEARN", "15 MINUTES"). |
| Entrance | Caption: opacity 0→1 over ~100 ms. Red title: 8 px blur→0 + opacity over ~250 ms, letters settling individually. Exit: caption cut; title blurs out. |
| Box / stroke / shadow | None. |
| Accents | Triple-stack B-roll (three 16:9 strips stacked vertically) crossfading in over ~400 ms; slow 3–5 % push-in on footage. Dark vignette. |

### 11. Grit · 9:16 · Bold, Motivation

| Attribute | Observed |
|---|---|
| Placement | Left-aligned bar, y ≈ 68 %, x from 6 % to ~70 % (bar width fixed per chunk, text left-aligned inside). |
| Font | Grotesk bold (Inter Bold), ALL CAPS, black on mint green (≈ #5CE6A5), ~30 px; single-word chunks grow to ~56 px and centre. |
| Reveal | **Word-by-word append inside a pre-sized bar.** The bar appears at full width first (blur-wipe ~60 ms), then words fill left→right. |
| Highlight | None by colour; emphasis via single-word chunk at larger size. |
| Entrance | Bar: 6 px blur→0 + opacity over ~60 ms (1–2 frames @30 fps). Words: cut on. Exit: cut. |
| Box | Solid mint rectangle, no radius, padding ≈ 0.4em. Slight 2° skew on title cards. |
| Accents | Skewed mint title block ("LEARNING") at y ≈ 5 % with distressed/scratch texture. Diagonal green-tinted B-roll panels slide in from the right (~300 ms). Picture-in-picture B-roll tiles pop in at corners. |

### 12. Velocity · 9:16 · Bold, Business

| Attribute | Observed |
|---|---|
| Placement | Centre, y ≈ 72 %. Single line. |
| Font | Heavy italic sans (Inter Black Italic), ALL CAPS, ~34 px. Plain words white; keyword **yellow** (≈ #FFE500). |
| Reveal | Word-by-word append, instant. |
| Highlight | Yellow colour on keyword. |
| Entrance | Instant. Exit: cut. |
| Box / stroke / shadow | No box; 2 px dark stroke + shadow. |
| Accents | **Big number slot-roll:** "100" appears top-left (y ≈ 5 %) as two stacked copies, white-on-top and gold-gradient-with-glow below; digits roll in individually over ~500 ms (12 frames @24 fps) with 10 px motion blur, then hold. Vertical scanline texture over the first second. Yellow diagonal wipe bar reveals B-roll from the bottom (~300 ms). |

### 13. Clarity · 9:16 · Minimal

| Attribute | Observed |
|---|---|
| Placement | Two-line block, centred, y ≈ 68 % (shifts to ≈ 85 % when the music-player card is up). |
| Font | Grotesk semibold ~40 px, white with 1 px dark stroke; sentence case. Emphasis chunks switch to **blue** (≈ #2F6BFF) when inside the white card. |
| Reveal | Whole chunk at once. |
| Highlight | Colour switch (white ↔ blue) by context, not per word. |
| Entrance | Opacity 0→1 + 3 px blur→0 over ~130 ms (4 frames @30 fps). Exit: fade ~100 ms. |
| Box / stroke / shadow | None on captions; the card UI has 24 px radius and 20 px soft shadow. |
| Accents | **Sticky-note stack:** three post-its (yellow, blue, pink) peel in with a page-curl over ~200 ms each, staggered ~300 ms, each tilted ±6°, then handwriting types on. **Music-player card:** white rounded card with album art, title, transport buttons and progress bar; the whole frame becomes a holographic gradient and the speaker video slides into a phone-like rounded rect (`easeInOut` ~500 ms). |

### 14. Sonnet · 16:9 · Trending, Minimal, Motivation

| Attribute | Observed |
|---|---|
| Placement | Centre-bottom, y ≈ 82 %. Up to two lines. Italic script title ("Learning.") top-left at y ≈ 10 %, x ≈ 2 %. |
| Font | Serif (Garamond-like) ~34 px, white, sentence case; keywords in **italic**. |
| Reveal | **Word-by-word append**; each word fades in over ~130 ms (4 frames @30 fps). |
| Highlight | Italic on keywords ("supercharge", "learning", "embrace"). |
| Entrance | Word fade. Exit: whole chunk cut. |
| Box / stroke / shadow | None. |
| Accents | Title fades in ~300 ms, holds across chunks, fades out ~300 ms. Light-leak flare pass at scene changes. Very slow push-in. |

### 15. Cinematic · 16:9 · Entertainment

| Attribute | Observed |
|---|---|
| Placement | Inside a letterboxed 2.39:1 frame with rounded corners; caption at y ≈ 80 % of the letterboxed picture. |
| Font | Serif bold (Times/Georgia) ~32 px, **yellow** (≈ #F4C542), sentence case. |
| Reveal | Whole chunk (2 words) at once. |
| Highlight | None. |
| Entrance | Instant. Exit: cut. |
| Box / stroke / shadow | 1 px dark stroke. |
| Accents | Film-reel open: black → horizontal slit expands (~250 ms) → colour flash → picture. Light leaks, scratches, vignette, warm grade. B-roll via film-burn transitions (~300 ms) and pillarboxed 4:3 inserts. |

### 16. Volt · 16:9 · Trending, Bold, Business

| Attribute | Observed |
|---|---|
| Placement | Centre-bottom, y ≈ 90 %. |
| Font | Geometric bold sans ~30 px. Plain words white regular; keyword **lime** (≈ #B8FF2E) bold italic at ~1.3×. |
| Reveal | Whole chunk at once. |
| Highlight | Lime colour + weight + italic. |
| Entrance | Opacity 0→1 + 6 px blur→0 over ~130 ms. Exit: cut; occasional white flash frame between scenes. |
| Box / stroke / shadow | No box; 1 px dark stroke. |
| Accents | Outlined-only (hollow) condensed italic title ("LEARNING STRATEGY") top-left at y ≈ 5 %, white stroke on dark, slight 3D offset stroke. Top title drifts upward ~2 % over its hold. |

### 17. Impact · 16:9 · Trending, Business, Motivation

| Attribute | Observed |
|---|---|
| Placement | Centre-bottom, y ≈ 88 %. |
| Font | Condensed bold (Bebas/Oswald), ALL CAPS, ~28 px; single-word emphasis chunk ~56 px. |
| Reveal | Whole chunk at once. |
| Highlight | Cyan (≈ #35D0FF) for the emphasis chunk, white for the rest (inverse of Impact II). |
| Entrance | Scale 1.1→1.0 + blur→0 + opacity over ~125 ms `easeOut`. Exit: cut. |
| Box / stroke / shadow | 2 px stroke + shadow. |
| Accents | Small emoji (🏋️) pops above the emphasis word, scale `easeOutBack` ~200 ms. Split-screen B-roll slides in from the right (~300 ms) with glitch. |

### 18. Ignite · 16:9 · Trending, Business, Motivation, New

| Attribute | Observed |
|---|---|
| Placement | Caption centred mid-frame, y ≈ 50 % (speaker's chest). Big keyword banner at y ≈ 90 %. |
| Font | Grotesk ~28 px; plain words white regular, keyword **red** (≈ #FF2A2A) bold. |
| Reveal | Word-by-word append; each word blurs in over ~100 ms. |
| Highlight | Red colour + weight. |
| Entrance | Blur/fade per word. Exit: cut. |
| Box / stroke / shadow | None. |
| Accents | **Full-screen red kinetic title:** frame fills with repeated outlined "BELIEVING" rows scrolling horizontally (3 rows, alternating direction, ~400 px/s), then crossfades into footage leaving one bold italic solid "BELIEVING" at the bottom with a red gradient band under it. Rainbow light-leak wipe (~250 ms) on the way in and out. Zoom punch-in ~5 % with white flash. |

### 19. Recess · 16:9 · Minimal, Motivation, Educational

| Attribute | Observed |
|---|---|
| Placement | Centre-bottom, y ≈ 90 %. |
| Font | Grotesk semibold ~26 px, white, sentence case. |
| Reveal | Whole chunk at once. |
| Highlight | None. |
| Entrance | Opacity + 3 px blur→0 over ~130 ms. Exit: fade ~100 ms. |
| Box / stroke / shadow | None. |
| Accents | B-roll card (16:9, 20 px radius) slides up from the bottom over ~400 ms `easeInOut` while the speaker video blurs (8 px) behind it; card slides back down the same way. Caption stays anchored to the frame, not the card. |

### 20. Pulse (basic) · 9:16 + 16:9 · Bold

| Attribute | Observed |
|---|---|
| Placement | 9:16: y ≈ 72 % centred. 16:9: dead centre (y ≈ 50 %) on a flat #1A1D1F preview background. |
| Font | Condensed bold (Oswald/League Gothic), ALL CAPS, ~40 px. |
| Reveal | **Line-by-line, two-line stack.** Line 1 appears, then line 2 fades in ~130 ms beneath it; next chunk replaces both. Words inside a line are already present. |
| Highlight | Keyword(s) in **cyan** (≈ #19C6FF); rest white. Entire line can be cyan when it is the emphasis line ("ADD CAPTIONS", "BOOST WATCH TIME"). |
| Entrance | Line: opacity 0→1 ~130 ms, sometimes with a slight 4 px rise. Exit: cut. |
| Box / stroke / shadow | 1 px dark stroke + 6 px glow in the text colour (cyan glow on cyan words). |
| Accents | None (pure caption style). |

### 21. Performance (basic) · 9:16 + 16:9 · Bold, Motivation

| Attribute | Observed |
|---|---|
| Placement | 9:16: y ≈ 73 % centred. 16:9: dead centre. |
| Font | Geometric bold (Montserrat ExtraBold), ALL CAPS. Keyword ~1.6× the size of plain words; plain words ~22 px white regular, keyword ~36 px **yellow** (≈ #EEFF00). |
| Reveal | **Line-by-line stack with per-word blur-in.** Line 1 appears; line 2 appears below ~300–600 ms later. New words blur in from 8 px over ~130 ms. |
| Highlight | Yellow + size + weight on the keyword; emphasis line entirely yellow. |
| Entrance | Blur-in per line. Exit: cut. |
| Box / stroke / shadow | 1 px stroke + soft shadow; yellow words get a 6 px yellow glow. |
| Accents | None. In 16:9 the caption is wider than the safe area at 1080p scale, which suggests the preview is rendered at a fixed size and not reflowed. |

---

## Part 2 — Cross-style summary: 7 recurring patterns

Each pattern is expressed as parameters a Premiere Pro (Essential Graphics / MOGRT) or After Effects template can implement. Defaults are the modal values across the 21 styles; ranges show the spread.

### Pattern A — Chunk cadence and placement (applies to every style)

| Parameter | Default | Range / notes |
|---|---|---|
| Words per chunk | 2 | 1–4; single-word chunks used for emphasis |
| Chunk duration | 900 ms | 400–2000 ms, follows speech; never shorter than 350 ms |
| Lines per chunk | 1 | 2 for the "line-stack" styles (Pulse, Performance, Clarity, Chalk) |
| Anchor y, 9:16 | 72 % | 68–78 % (Prism Pro is the outlier at the top, 3–12 %) |
| Anchor y, 16:9 | 88 % | 80–90 %; preview-only "basic" styles centre at 50 % |
| Anchor x | 50 % | Grit and Prism Pro left-align at 6 % |
| Safe width | 80 % of frame | text wraps at this width; never reflows after appearing |
| Chunk exit | hard cut | only Elevate, Clarity, Recess fade out (80–100 ms) |

### Pattern B — Word-fill karaoke (Paper II, Prime, Sonnet, Ignite, Y2K, Velocity, Chalk)

The chunk is fully laid out at the start; each word transitions as it is spoken. Layout is fixed so nothing shifts.

| Parameter | Default | Range |
|---|---|---|
| Inactive word opacity | 40 % | 0 % (append styles: Y2K, Velocity, Grit) to 45 % |
| Active transition | opacity 40→100 % | optional blur 3 px→0 |
| Transition duration | 100 ms | 80–130 ms |
| Easing | `easeOut` | |
| Scale on activate | none | Chalk keywords 1.1→1.0 |

### Pattern C — Blur-pop entrance (Impact, Impact II, Volt, Clarity, Recess, Performance, Elevate, Form, Grit bar)

The most common whole-chunk entrance.

| Parameter | Default | Range |
|---|---|---|
| Opacity | 0→100 % | |
| Gaussian blur | 6 px→0 | 3–8 px |
| Scale | 1.10→1.00 | 1.00 (no scale) to 1.15 |
| Duration | 125 ms | 80–150 ms (2–4 frames) |
| Easing | `easeOut` | |
| Exit | cut | |

### Pattern D — Keyword emphasis

Every style marks one word per chunk; the mechanism varies but combines at most two of these.

| Mechanism | Styles | Parameter |
|---|---|---|
| Colour | Pulse (cyan), Performance (yellow), Velocity (yellow), Volt (lime), Ignite (red), Chalk (yellow), Impact/Impact II (cyan vs white) | accent colour from the style's `colorPresets`; plain words stay white |
| Weight | Pop, Form, Prism Pro, Volt, Ignite | regular → bold (or bold italic) |
| Italic | Elevate, Sonnet, Form, Prism Pro | same face, italic |
| Size | Performance (1.6×), Prism Pro (1.6×), Grit single-word (1.9×), Impact single-word (2×), Form (1.3×) | size ratio relative to plain words |
| Glow | Pulse, Performance, Velocity numbers | outer glow 6 px in the accent colour at 60 % |

Recommended template default: colour + bold, size 1.0; expose a "big word" toggle that sets size 1.6× and centres the chunk.

### Pattern E — Box / pill treatments (Paper II, Pop, Chalk, Grit)

| Parameter | Pill (Paper II, Pop) | Bar (Grit) | Line pill (Chalk) |
|---|---|---|---|
| Fill | #F2F2F2 @ 92 % or #FFF | accent solid (#5CE6A5) | #222 @ 85 % |
| Radius | 50 % of height | 0 | 8 px |
| Padding | 0.5em × 0.3em | 0.4em × 0.25em | 0.4em × 0.2em |
| Outline | none / 2 px black (Pop) | none | none |
| Shadow | 8 px @ 20 % | none | none |
| Sizing | fits final chunk, fixed | fixed width per chunk, text fills left→right | grows per word |
| Entrance | blur 2 px→0 + opacity, 80 ms | blur 6 px→0, 60 ms, then words cut on | with first word |

Non-boxed styles use: 1–2 px dark stroke (≈ #000 @ 60 %) + drop shadow 6–8 px, 40 %, 0 offset.

### Pattern F — Parked title / big-word card (Prism Pro, Prime, Elevate, Ember, Grit, Volt, Velocity, Ignite, Sonnet, Chalk, Paper II)

A second text layer that persists across 3–8 chunks, separate from the captions.

| Parameter | Default | Range / notes |
|---|---|---|
| Position | top-left, y 5 %, x 4 % | Ember parks at y 50 %; Ignite at y 90 % |
| Size | 2.5× caption size | 2–4× |
| Style | ALL CAPS condensed or script, accent colour | hollow outline (Volt), skewed block (Grit), gradient + glow (Velocity) |
| Entrance | blur 8 px→0 + opacity, 250 ms | type-on 40 ms/char (Paper II, Chalk draw-on 200 ms); slot-roll 500 ms (Velocity) |
| Hold | 3–5 s | |
| Exit | blur out 250 ms | type-off 40 ms/char (Form) |
| Drift | none | Volt drifts up 2 % over hold |

### Pattern G — Scene accents (B-roll, zoom, stickers)

| Accent | Styles | Parameters |
|---|---|---|
| Zoom punch-in | Prism Pro, Prime, Impact II, Ignite | scale 1.00→1.05–1.08 over 200–250 ms `easeOut` at chunk start; optional 1-frame white flash |
| B-roll slide-in card | Recess, Elevate, Grit, Impact, Velocity | from bottom or right, 300–400 ms `easeInOut`, 20 px radius, background blur 8 px while up |
| Diagonal panel wipe | Form, Grit, Velocity | solid accent panel, 15–20° skew, 250–300 ms `easeInOut` |
| Sticker pop | Pop, Paper II, Clarity | scale 0→1 `easeOutBack` 200–300 ms, stagger 60–100 ms, rotation ±6–15° |
| Glitch / RGB split | Impact II, Impact | 150–200 ms, ±6 px channel offset, at scene changes only |
| Light leak / film burn | Cinematic, Sonnet, Ignite | 250–300 ms additive overlay on cuts |
| Emoji | Impact only | one emoji above the emphasis word, `easeOutBack` 200 ms |

### Suggested MOGRT parameter set

```
chunk:        wordsPerChunk=2, minHoldMs=350
layout:       anchorY=72% (9:16) | 88% (16:9), anchorX=50%, maxWidth=80%, lines=1
font:         family, size=48 (9:16) | 30 (16:9), case=upper|sentence|lower
reveal:       mode=wordFill|whole|lineStack, inactiveOpacity=40%, wordMs=100
entrance:     opacity 0→1, blurPx=6→0, scaleFrom=1.10, durationMs=125, ease=easeOut
exit:         mode=cut|fade, durationMs=80
emphasis:     color=#accent, weight=bold, italic=false, sizeRatio=1.0, glowPx=0
box:          mode=none|pill|bar|linePill, fill, radius, padX=0.5em, padY=0.3em, outlinePx=0
stroke:       px=1, color=#000@60%   shadow: px=6, opacity=40%
title:        enabled, text, posY=5%, sizeRatio=2.5, inMs=250, holdMs=4000, outMs=250
accents:      punchIn=5%/250ms, brollSlide=400ms, stickerPop=250ms/easeOutBack
```

### Notes and caveats

- All timings come from frame counting at 24–30 fps; anything listed as 80–130 ms is 2–4 frames and could not be measured more finely.
- Colours are read off compressed previews; use the `colorPresets` hex values from the catalog JSON where they exist (most premium styles list five).
- Preview clips for the "basic" tier are rendered captions on a flat background, so their placement (dead centre in 16:9) is not representative of in-app output.
- Fonts are identified by appearance only; no font files or CSS were available.

---

## Part 3 — The other 33 premium styles (compact specs)

Second pass, 2026-10-17. Same method as Part 1 (first 4 s at 10 fps on a contact sheet), one line per style. "Append" = words are added as spoken with layout fixed; "fill" = whole chunk laid out, words activate; "whole" = chunk appears at once. Positions are the measured band centre from `measurements.csv`.

| Style | Ratio | y % | Caption font / case | Reveal | Emphasis | Box / stroke | Signature accent |
|---|---|---|---|---|---|---|---|
| Align | 9:16 | 59 | Monospace, ALL CAPS, black on white box once on footage | append | none | white box, square corners | Opens on a white card: mono title "COMPUTERS" top, subtitle letters scramble in; footage fades under |
| Analog | 9:16 | 47 | Rounded heavy sans, white, lower case | append, each word rises 4 px + fades (~100 ms) | size (keyword 1.3×) | none, soft shadow | Green ✦ star cluster pops on the speaker; cut to full white card with green "STRENGTHENING"; fade out/in 250 ms |
| Archive | 9:16 / 16:9 | 64 / 53 | Condensed bold, ALL CAPS, white | **fill, inactive words hollow (stroke only)** then fill solid | none | none | Hollow-outline inactive state is the only one of its kind; 2–3 word stacks |
| Bloom | 9:16 | 67 | Rounded sans, lower case, small | append | size (keyword 1.4×) | none | Arch-shaped (rounded top) mask around speaker; serif "MOISTURIZE" + script "Routine" title |
| Blueprint | 9:16 | 69 | Grotesk, ALL CAPS, white | fill, inactive grey; **active word gets an underline that draws left→right** | underline | none | Graph-paper background; footage window scales in from a point (~500 ms) with blue selection handles; hollow blue "INTRODUCING" title |
| Byline | 9:16 / 16:9 | 65 / 81 | Grotesk, sentence case, small | whole, fade ~100 ms | size on single-word chunks | none | Split-screen grid, black-and-white B-roll tiles sliding in |
| Cinematic II | 9:16 | 73 | Serif, yellow (#F4C542) | whole | none | 1 px stroke | Film-reel slit open, sprocket-hole frame overlay, light leaks, rainbow flare |
| Core | 9:16 | 69 | Grotesk regular, white | append, second line appended below | **red** (#E8302A) keyword | none | Thin red rule at top; hatched "blueprint" title box; grid lines |
| Evo | 9:16 | 73 (title) / 12 (caption) | Grotesk; caption small at top of card | append, blur-in per word | bold italic + 1.3× | none | Speaker inside a blue-gradient rounded frame; huge bold italic "THE KEYS TO INVESTING" at bottom; later the frame floats over a holographic gradient with B-roll cards |
| Film | 9:16 | 67 | Serif, yellow, small | whole | none | none | Black rounded border; yellow condensed "MEMORIES" types on letter by letter (~5 frames) with glitch jitter |
| Focus | 9:16 | 70 | Grotesk, small, lower case | fill; **active word gets a solid white box** (black text) that jumps word to word | box | white box on active word only | Solid blue (#2F55FF) band slides up from the bottom (~300 ms) carrying a big "FOLLOWERS"; later stacked blue panels wipe through |
| Growth | 9:16 | 50 | Grotesk bold, ALL CAPS, white, 2 lines | whole | **red** single-word chunk at 1.6× | none | Red rectangular outline scales around the speaker; black grid stage with B-roll strip |
| Kai | 9:16 | 52 | Rounded sans, lower case | append; **active word gets a green→blue gradient pill** | gradient pill | pill on active word | Background blurs 8 px on hook; arch mask; gradient backdrop; ✦ sparkle |
| Lens | 9:16 | 65 | Monospace, ALL CAPS, left-aligned in black bar | append inside a pre-sized bar | none | black bar | Camera HUD frame with exposure readout; orange "Aperture" types on letter by letter; footage scales in from a point; light leak |
| Lift | 9:16 | 74 | Grotesk, lower case | append; **active word in mint pill** (#5FD39A), inactive 60 % | pill | pill on active word | Mint diagonal panel wipes in from top-right (~300 ms); serif "Your Team" title |
| Linen | 9:16 | 73 | Serif italic, dark on pale-pink pill | whole, fade ~100 ms | none | pill #F3DDD0, radius 4 px | Serif "WEAR" + italic "your style" title; cream diagonal panel with "Just dropped" |
| Lumen | 9:16 | 68 | Grotesk, white on dark-brown bar | append, left-aligned in a **pre-sized full-width bar** | none | bar #3D332E, no radius | Paper-grid background; footage in rounded rect scales in; small serif "Vision" label |
| Magazine | 9:16 | 48 | Grotesk, white, sentence case | append; active word flashes **purple → white** (~130 ms) | colour flash | none | Speaker in a letterboxed photo frame over grey; script "Scrolling" types on; polaroid collage with black pill + yellow keyword |
| Neon | 9:16 | 70 | Rounded sans, white, two lines | append | **pink glow** keyword (#FF4FD8) | none | Neon-sign collage (pink/blue/green) flickers on around the speaker; script neon title |
| Orbit | 9:16 | 68 | Serif italic, white on blue pill | whole; pill scales 0.9→1 (~150 ms) and resizes to the text | italic keyword | pill #2F5BBF, radius full | Condensed "FRIENDS" slides in from the top and holds |
| Pulse (premium) | 9:16 | 60 | Condensed bold, ALL CAPS, white + cyan | **line stack**, blur-in per line | cyan (#19C6FF) line | cyan glow | Dark grid of rounded tiles; footage tile scales in; HUD feel |
| Rebel | 9:16 | 64 | Serif, yellow/white on black label | append | yellow keyword | black label | Yellow spray-paint strokes and crown; halftone speech-bubble collage; ransom-note rotated labels |
| Rocket | 9:16 | 60 | Rounded condensed, ALL CAPS, white | append, inactive lavender | lavender → white | none | Diagonal light-streak wipes; chromatic lens-blur transition; small "INDIE COMEBACK" title grows |
| Sketch | 9:16 | 64 | Handwritten marker, white | append | none | later: dark strike-through bar | "MIND MAP" title with a hand-drawn ellipse scribbled on (~250 ms); marker scribble boxes |
| Stack | 9:16 | 67 | Rounded sans, mixed size | append; keywords in **red pills** (#E8392E), plain words small white | pill + size | pill on keywords | Two-tone "TECHNOLOGY" title; footage in rounded rect; white flash transitions |
| Story | 9:16 / 16:9 | 54 / 77 | Serif, white | append | **yellow italic** keyword | none (white pill on B-roll) | Serif "Mentoring" title fades in top-left; B-roll gets a white pill caption |
| Vinyl II | 9:16 | 65 | Grotesk, dark on cream box | append inside pre-sized box | **orange** keyword (#FF4A1C) | cream box, square | Orange bands top and bottom with repeated "AUTHENTIC" letters scrambling in; bands slide in/out |
| Vista | 9:16 | 67 | Serif, white, small | append | none | none | Large hollow serif "REALTY" title; grey stepped geometric panels; triangle-pattern transition |
| Zine | 9:16 | 62 | Handwritten italic, ALL CAPS, white | append, two lines | none | none | Paper-cutout blue cloud with bold "DIY ZINES"; doodles; scissors cut-out |
| Paper | 16:9 | 83 | Rounded sans in white pill | fill (active dark, inactive grey) | weight | pill, radius full | Serif "parallel play" title with offset drop shadow; torn-paper blue panel with black label + sticker |
| Prism Pro | 16:9 | 55 | As 9:16 (top-left stack) | fill | bold italic gradient keyword | none | Same as 9:16; title block sits lower in the frame |
| Elevate / Recess / Sonnet / Volt / Ignite | other ratio | see CSV | as Part 1 | as Part 1 | as Part 1 | as Part 1 | Orientation siblings; only placement changes |

### New mechanisms surfaced by this pass (add to Pattern D and E)

| Mechanism | Styles | Parameters |
|---|---|---|
| **Moving highlight box** on the active word | Focus (white box), Lift (mint pill), Kai (gradient pill), Stack (red pill on keywords only) | box fits the word with 0.3em × 0.15em padding; jumps (no tween) to the next word on its start; inactive words 60 % opacity |
| **Hollow inactive words** | Archive | 2 px stroke, no fill → solid fill on activation, 80 ms |
| **Underline draw** | Blueprint | 3 px rule under the active word, wipes left→right over ~130 ms |
| **Pre-sized bar, left-aligned fill** | Grit, Lumen, Lens, Vinyl II | bar appears first at final width (blur 6 px→0, 60 ms), then words cut on |
| **Type-on titles** | Film, Lens, Magazine, Paper II, Chalk | 40 ms per character, optional 1-frame glitch jitter |
| **Letter scramble-in titles** | Align, Vinyl II | random glyphs resolve left→right over ~300 ms |
| **Footage scales in from a point** | Blueprint, Lens, Lumen, Pulse | scale 0→1 over 400–500 ms `easeOutBack`, with selection-handle or HUD frame |

---

## Part 4 — Basic caption presets (`caption-styles` endpoint)

`GET https://internal.captions-api.com/studio-go/caption-styles?pageSize=100` returns 67 flat caption presets (saved in `caption-styles.json` / `caption-styles.md`). 47 of them also appear in `ai-edit-styles.json` tagged `basic`; 20 exist only here (Baseline, Chronicle, Closed Cap, Daily Mail, Doodle, Eclipse, Energy II, Flair, Footprint v3, Fuel, Garnet, Helios, Hustle v3, Lilac, Linear, Minima, Note, Poem, Scene, Script).

Each preset carries a 4-slot `colors` array. Reading eight previews against their arrays:

| Slot | Meaning (inferred) | Evidence |
|---|---|---|
| 0 | Base text fill | white in 66 of 67 presets |
| 1 | Active / emphasis word colour | Heat `#FF0000` = red "Hey,"; Pulse `#14C7FF` = cyan line; Aries/Dimidium `#F7CE45`/`#FEF894` = yellow "HEAR" |
| 2 | Stroke, shadow or container | `#000000` where a dark stroke/shadow shows (Aries, Dimidium, Marigold); `#999999` on Heat = upcoming-word grey; `#1E89FE` on Messages = blue bubble |
| 3 | Glow or secondary accent | Marigold `#FDE300` yellow glow; Messages `#9AD14B` = alternate green bubble; often repeats slot 0 or 1 |

Caveat: container backgrounds are not always in the array (Dimidium's purple box is not listed), so treat slot 2/3 as "secondary colours the renderer may use" rather than a strict schema.

Preview behaviour (all 67 are 1920×1080 at 32 fps, 4.9 s, flat `#1A1D1F` background, same script "Hey, did you hear about the bakery in…"):

- 44 of 56 confidently measured presets reveal **whole chunks**; 12 reveal **word by word** (Aries, Baseline, Cove, Eclipse, Energy II, Marigold and six more).
- Median chunk hold **1.09 s** (IQR 0.81–1.62 s), roughly twice the premium styles, because the previews are rendered at a slower reading pace.
- Median entrance **47 ms** (1–3 frames): basic presets mostly cut on. The exceptions that animate for ~500 ms are Alcyone, Arion Pink and Cartwheel Purple (scale/bounce).
- Band centre median **47 %**: dead centre, not representative of in-app placement.

---

## Part 5 — Measured values (`measurements.csv`, `tools/measure_captions.py`)

Method: every preview decoded at native fps, scaled to 360 px wide. "Text" = pixels that are bright or saturated and have strong 7 px local contrast. The densest 12 %-high band in the lower 60 % of frame (whole frame for 16:9) is the caption band. A **chunk boundary** is a frame where the band mask keeps < 25 % overlap with the previous frame while the footage under the band did not cut; a **word event** keeps 50–90 % overlap and grows the mask by > 20 %. Entrance = frames after a boundary until the band stops changing (> 6 % per frame), capped at 0.5 s.

| Group | n | Band y % median (IQR) | Chunk hold s median (IQR) | Entrance ms median (IQR) | Word-by-word styles |
|---|---|---|---|---|---|
| Premium 9:16 | 45 | **67.4** (64.2–69.8) | **0.53** (0.38–0.82) | **208** (102–468) | 3 (Orbit, Sonnet 9:16, Zine) |
| Premium 16:9 | 12 | **77.0** (69.7–80.3) | 0.65 (0.47–0.78) | 178 (83–354) | 0 |
| Basic presets | 56 | 47.2 (41.7–50.0) | 1.09 (0.81–1.62) | 47 (31–101) | 12 |

What this corrects in Parts 1–2:

- **Anchor y for 9:16 is 67 %, not 72 %.** The eyeballed 72 % was biased by the few styles with pills; the measured band centre across 45 styles is 67 % with a tight IQR. Use 66–70 % as the default range and 1450–1600 px as the SOP-safe zone check.
- **Chunk holds are shorter than estimated**: median 0.53 s in 9:16 previews, with a floor around 0.28 s (Paper II, Lumen). The 350 ms minimum in Pattern A stands.
- **Entrances are bimodal.** About half the 9:16 styles settle within 100 ms (cut or 2-frame fade). The other half register 350–500 ms, which is not a longer fade: it is the word-append styles, where the band keeps changing for the length of the chunk. For whole-chunk styles the 80–150 ms blur-pop in Pattern C holds; for append styles use per-word cut-ons.
- Word-by-word detection undercounts: the detector classifies most append styles as "chunk" because each appended word changes the mask by less than the 20 % growth threshold on long lines. The visual pass (Parts 1 and 3) is authoritative for reveal mode; the CSV is authoritative for placement and hold.

Columns in `measurements.csv`: `file, w, h, fps, dur_s, band_conf` (fraction of frames with a detected band; trust rows ≥ 0.8), `band_y_pct, band_y_iqr_pct, chunks, word_events, word_events_per_s, reveal, chunk_hold_med_s, chunk_hold_min_s, entrance_med_frames, entrance_med_ms, entrance_p90_ms, accents` (up to three quantised accent colours seen inside the band).

Low-confidence rows to ignore: Prism Pro 9:16 (captions at top of frame), Poem, Growth, Heat, Alhena (dark or scripted text the mask misses), Cartwheel Black, Cygnus A, Drive, Million, Monster, Orion, Scene.

Run it again with:

```bash
python3 -I tools/measure_captions.py previews/*.mp4 previews/caption-styles/*.mp4 --out measurements.csv
```
