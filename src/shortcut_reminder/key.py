from enum import Enum
from pathlib import Path
from PIL import Image


class Key(Enum):
    CTRL = "ctrl"
    SHIFT = "shift"
    HOME = "home"
    END = "end"
    UP = "cursor-up"
    DOWN = "cursor-down"
    LEFT = "cursor-left"
    RIGHT = "cursor-right"
    A = "a"


ASSETS_DIR = Path(__file__).resolve().parent / "assets" / "images" / "keys"


def load_key_icon(path: Path) -> Image.Image:
    with Image.open(path) as image:
        image = image.convert("RGBA")
        width, height = image.size
        new_width = round(width * 60 / height)

        return image.resize(
            (new_width, 60),
            Image.Resampling.LANCZOS,
        )


KEY_ICONS = {
    key: load_key_icon(ASSETS_DIR / f"{key.value}.png")
    for key in Key
}
