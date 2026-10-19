# Design mockups

These files are design changes for the home page, made on a Claude Design canvas.
They are now implemented in `layouts/index.html`, `layouts/partials/petiole.html`,
`layouts/partials/theme_css.html` and `config.json`; the files here are kept for reference.

| File | What it is |
| --- | --- |
| `home-light.dc.html` | Revised home page, light mode |
| `home-dark.dc.html` | Revised home page, dark mode |
| `petiole-light.svg` | Hero diagram: petiole in transverse section, colored as safranin/astra blue (phloem blue, xylem red) |
| `petiole-dark.svg` | Same diagram for dark mode, phloem in fluorescent green |

The `.dc.html` files are canvas source; they load the canvas runtime (`support.js`) and
won't render on their own. Open the SVGs directly, or read the HTML for layout and colors.

## Changes from the current theme

- Intro reframed: environmental scientist at Stantec, with the plant anatomy and physiology work as background.
- Hero micrograph replaced by a schematic petiole diagram (seven collateral bundles in a ring around a larger medullary bundle); no circular frame or scale bar; caption without a figure number.
- Nav shortened to About, CV, Writing.
- "Current research" renamed "Research, 2019–2025".
- "Recent posts" replaced by "Selected publications" (five items), with links to Writing and Notes below.
- Dark mode: near-black green ground, pale text, green link accent, fluorescent-green phloem.
