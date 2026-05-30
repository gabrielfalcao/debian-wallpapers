# coding: utf-8
import os
from pathlib import Path

here = Path(".")

def gen_png_image(title, png):
    return f"[![{title}](https://github.com/gabrielfalcao/debian-wallpapers/raw/refs/heads/main/{png.name})](https://github.com/gabrielfalcao/debian-wallpapers/raw/refs/heads/main/{png.name})"

print(
    "\n".join(
        [
            gen_png_image(title, png)
            for (title, png) in [
                (os.path.splitext(png.name)[0].replace("-", " "), png)
                for png in here.glob("*.png")
            ]
        ]
    )
)
