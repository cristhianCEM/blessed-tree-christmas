from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache

SIZE_DRAW = (20, 34)
DEFAULT_FONT = 'consola.ttf'
DEFAULT_FONT_SIZE = 18
WHITE_COLOR = (255, 255, 255)

@lru_cache(maxsize=None)
def count_drawn_pixels(character: str) -> int:
    image = Image.new('RGB', SIZE_DRAW, 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(DEFAULT_FONT, DEFAULT_FONT_SIZE)
    draw.text((5, 10), character, fill='black', font=font)
    non_white_pixels = sum(pixel != WHITE_COLOR for pixel in image.getdata())
    return non_white_pixels