# Hanumant Shinde Portfolio

A Python Flask personal portfolio website built from the 2026 resume content.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Build static files for free hosting

```bash
source .venv/bin/activate
python build_static.py
```

The deployable static site will be created in `dist/`.

## Publish updates to GitHub Pages

This repository serves GitHub Pages from the `master` branch, folder `docs/`.

```bash
python build_static.py
git switch master
rm -rf docs
mkdir docs
cp -R dist/. docs/
touch docs/.nojekyll
git add docs
git commit -m "Update portfolio site"
git push
git switch main
```

## Customize

Most content lives in `app.py` as Python dictionaries and lists. The layout is in `templates/index.html`, with visual styling in `static/styles.css`.
