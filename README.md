# Maruthiruvar & Velu Nachiyar: intro booklet

Quick intro for middle/high schoolers attending the stage play about the Maruthu brothers and Queen Velu Nachiyar.

## Layout
- `poster.html`: page 1, the heroes (maroon/gold palette, filigree frame)
- `plot.html`: page 2, the story, route map and timeline (`?theme=parchment` for the print palette)
- `assets/images/`: character portraits
- `plot2.html`: play guide, two pages following the dance-drama's flow, with "In the play" scene tags
- `story.html`: two-page story in historical order, no play references; clearer map (Tamil Nadu overview + Sivaganga zoom inset). Optional scene art goes in `assets/scenes/` (see its README)
- `tools/`: generators (`gen2.py` -> plot2, `gen3.py` + `mapgen.py` -> story); they currently read from `/tmp`, so adjust paths before re-running
- `reference/gemini_original.html`: first Gemini draft, kept for reference

## Planned outputs
- Mobile web page (QR code target), hosted on GitHub Pages/Netlify
- A4 3-page print PDF
- A3 poster
