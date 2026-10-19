# dustinray-theme

A custom [Micro.blog](https://micro.blog) theme for [dustinray.net](https://www.dustinray.net), built around plant micrographs.

The home page opens on a single micrograph shown as a circular "field of view", with a scale bar and a figure caption. Research and photo posts are listed as posts; older short posts live in a separate Notes section.

## What's in the repo

```
config.json   Micro.blog site config, plus this theme's settings (see below)
layouts/      Hugo templates (home, posts, pages, archive, notes, photos, feeds)
dev/          Sample content and a config generator for local previews
scripts/      dev.sh: build or serve the theme locally
```

A Micro.blog theme is just `config.json` and `layouts/`. The feed, podcast, RSD and sitemap templates come unchanged from Micro.blog's [theme-blank](https://github.com/microdotblog/theme-blank) (MIT, see `LICENSE-microblog-blank`). Everything else is new.

The stylesheet lives in `layouts/partials/theme_css.html` as an inline `<style>` block, so it doesn't depend on how Micro.blog serves static files.

## Settings

Edit these under `params` in `config.json`.

| Setting | What it does |
| --- | --- |
| `tagline`, `intro` | Heading and paragraph beside the micrograph |
| `hero.image` | URL of the micrograph (it is cropped to a circle) |
| `hero.alt` | Alt text for the micrograph. Describe what it shows. |
| `hero.title`, `hero.detail` | Figure caption. HTML is allowed, so `<i>Lupinus</i>` works. Leave both empty for no caption. |
| `hero.scale_label`, `hero.scale_percent` | Scale bar, e.g. `"50 µm"` and `20`. The percent is the bar's length as a share of the circle's diameter as displayed, so measure it against the cropped image. Leave either empty to hide the bar. |
| `research_highlights` | Items under "Current research" on the home page |
| `main_categories` | Categories that count as main posts (see below) |
| `notes_intro` | Sentence under the Notes heading |
| `nav` | Header navigation |

## Posts and Notes

A post is listed under **Posts** (the home page and `/archive/`) when it has at least one category in `main_categories`. Every other post goes to **Notes** at `/notes/`. Nothing is hidden: Notes posts keep their URLs, still appear in your feeds, and still show up on category pages.

To move a post, add or remove a category in Micro.blog. To change the rule, edit `main_categories`.

## Previewing locally

You need [Hugo](https://gohugo.io) 0.91.x (the version the site reports) and Python 3.

```sh
scripts/dev.sh serve   # http://localhost:1313
scripts/dev.sh build   # writes ./public
```

The preview uses the sample posts in `dev/content` and a generated config (`dev/config.json`, not committed). It shows placeholder micrographs, not your real ones.

## Using it on Micro.blog

Micro.blog can create a custom theme by cloning a GitHub repository (Design, then Edit Themes). The menu names have changed over the years, so check the [help pages](https://help.micro.blog) if you don't see them.

After importing, check:

1. `config.json` kept Micro.blog's `[PLACEHOLDER]` values; Micro.blog fills those in when it builds the site.
2. The Archive, Photos and Notes pages load (`/archive/`, `/photos/`, `/notes/`).
3. The About and CV pages still appear at `/about/` and `/cv/`. If you move them, update `nav` and `research_highlights`.

## Fonts

Newsreader and Public Sans load from Google Fonts. To avoid calling Google, delete the three font `<link>` lines in `layouts/partials/head.html`; the CSS falls back to Georgia and the system sans-serif.

## License

MIT. See `LICENSE`, and `LICENSE-microblog-blank` for the files derived from Micro.blog's blank theme.
