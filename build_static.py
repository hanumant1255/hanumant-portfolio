from pathlib import Path
from shutil import copytree, rmtree

from app import app


ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def build() -> None:
    if DIST.exists():
        rmtree(DIST)

    (DIST / "static").mkdir(parents=True)

    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise RuntimeError(f"Static build failed with status {response.status_code}")
        html = response.get_data(as_text=True)

    html = html.replace('/static/', 'static/')
    (DIST / "index.html").write_text(html, encoding="utf-8")
    copytree(ROOT / "static", DIST / "static", dirs_exist_ok=True)


if __name__ == "__main__":
    build()
    print(f"Built static site at {DIST}")
