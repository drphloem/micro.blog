#!/usr/bin/env python3
"""Build dev/config.json from the theme's config.json.

micro.blog fills the [PLACEHOLDER] values when it builds your site. For local
previews we fill them with sample values and point Hugo at the theme layouts.
"""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
text = (root / "config.json").read_text()

values = {
    "TITLE": "Dustin Ray, PhD",
    "FULL_NAME": "Dustin Ray",
    "USERNAME": "dustinray",
    "SCHEME": "http",
    "HOSTNAME": "localhost:1313",
    "LANGUAGE": "en",
}
text = re.sub(r"\[([A-Z_]+)\]", lambda m: values.get(m.group(1), ""), text)
cfg = json.loads(text)

cfg["layoutDir"] = "../layouts"
cfg["params"]["hero"].update({
    "image": "/img/sample-plate.svg",
    "alt": "Sample micrograph: a grid of stained cells",
    "title": "Fig. 1. Sample plate.",
    "detail": " Placeholder cells in safranin and fast green. Replace with your own micrograph in config.json.",
    "scale_label": "50 µm",
    "scale_percent": 28,
})

(root / "dev" / "config.json").write_text(json.dumps(cfg, indent=2))
print("wrote dev/config.json")
