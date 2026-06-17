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

## Customize

Most content lives in `app.py` as Python dictionaries and lists. The layout is in `templates/index.html`, with visual styling in `static/styles.css`.
