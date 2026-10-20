# dustinray-theme

A custom [Micro.blog](https://micro.blog) theme for [dustinray.net](https://www.dustinray.net), built around plant micrographs.

The home page opens on a single micrograph shown as a circular "field of view", with a scale bar and a figure caption. Research and photo posts are listed as posts; older short posts live in a separate Notes section.

## What's in the repo

```
config.json   Micro.blog site config, plus this theme's settings (see below)
layouts/      Hugo templates (home, posts, pages, archive, notes, photos, feeds)
content/      Source copy for pages that live in Micro.blog (cv.md); paste into the page, not read by the theme
dev/          Sample content and a config generator for local previews
scripts/      dev.sh: build or serve the theme locally
```

A Micro.blog theme is just `config.json` and `layouts/`. The feed, podcast, RSD and sitemap templates come unchanged from Micro.blog's [theme-blank](https://github.com/microdotblog/theme-blank) (MIT, see `LICENSE-microblog-blank`). Everything else is new.

The stylesheet lives in `layouts/partials/theme_css.html` as an inline `<style>` block, so it doesn't depend on how Micro.blog serves static files.

## Settings

Edit these under `params` in `config.json`.

| Setting | What it does |
| --- | --- |
| `tagline`, `intro` | Heading and paragraph beside the petiole diagram |
| `intro_questions` | The numbered questions at the end of the intro. Each links to the first publication whose `goals` contains its `id`. |
| `intro_note` | Smaller line under the intro. Leave empty to hide it. |
| `altmetric` | `true` shows an Altmetric badge on each publication with a DOI link (loads a script from altmetric.com). Badges stay hidden until a paper has mentions. `false` turns it off. |
| `publications` | "Selected publications" on the home page: `year`, `title`, `citation` (HTML allowed), `url` (may be empty), `goals` (list of question ids, e.g. `["2"]`, shown as numbered badges) |
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
3. The About and CV pages still appear at `/about/` and `/cv/`. If you move them, update `nav`.

## Fonts

Newsreader and Public Sans load from Google Fonts. To avoid calling Google, delete the three font `<link>` lines in `layouts/partials/head.html`; the CSS falls back to Georgia and the system sans-serif.

## License

MIT. See `LICENSE`, and `LICENSE-microblog-blank` for the files derived from Micro.blog's blank theme.
