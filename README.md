# Marudhiruvar: heroes of Sivaganga

Bilingual (English/Tamil) intro for middle/high school students attending the stage play about the Maruthu brothers and Queen Velu Nachiyar. Static HTML, no build step; each page has a dark theme and a parchment theme (`?theme=parchment`).

## Pages
- `index.html`: landing page (the QR code points here)
- `story.html`: two-page story in historical order, with map, zoom inset and timeline
- `poster.html`: one-page heroes poster
- `play-guide.html`: two pages following the dance-drama's scene flow, with "In the play" tags
- `downloads/`: A4 PDFs of the three pages above, dark and parchment

## Files
- `assets/images/`: character portraits
- `assets/fonts/`: local web fonts (Cinzel, Noto Sans/Serif Tamil)
- `assets/theme.js`: dark/light theme. The landing page has the switch (☀️/🌙); the other pages follow the saved choice; `?theme=dark|light` overrides
- `assets/mobile.css`: phone layout (screen only; print/PDF unaffected)
- `assets/qr.svg`: QR code for `https://anbu25.github.io/marudhiruvar/`
- `assets/scenes/`: optional scene art slots (see its README)
- `reference/`: first Gemini draft and palette options
- `tools/`: `gen2.py` builds `play-guide.html`; `gen3.py` + `mapgen.py` build `story.html` (run `python3 tools/gen3.py`). `tnmap.py` was a one-off that produced the map data.

## Exporting PDFs
```
chrome --headless --no-pdf-header-footer --print-to-pdf=downloads/story_a4_dark.pdf story.html
chrome --headless --no-pdf-header-footer --print-to-pdf=downloads/story_a4_parchment.pdf "story.html?theme=parchment"
```

## Open items
- Verify facts against print sources; native-speaker check of the Tamil
- Scene art (`assets/scenes/`) not generated yet
