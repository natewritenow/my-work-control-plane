"""Inline the icon sprite into src.html and write index.html."""
from pathlib import Path

here = Path(__file__).parent
sprite = (here / "icons.svg").read_text()
src = (here / "src.html").read_text()
(here / "index.html").write_text(src.replace("<!--SPRITE-->", sprite))
print("wrote index.html")
