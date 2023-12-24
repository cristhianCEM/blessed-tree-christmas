import colorsys
from typing import List


def rgba_to_hsl(r: int, g: int, b: int, alpha: float = 1) -> List[float]:
    """
    Converts an RGBA color to HSL color space.

    Args:
        r (int): The red component of the color (0-255).
        g (int): The green component of the color (0-255).
        b (int): The blue component of the color (0-255).
        alpha (float, optional): The alpha (opacity) value of the color (0-1). Defaults to 1.

    Returns:
        List[float]: The HSL representation of the color [h, s, l, alpha].
    """
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return [h * 360, s * 100, l * 100, alpha]


def hsl_to_rgba(h: float, s: float, l: float, alpha: float = 1) -> List[int]:
    """
    Converts an HSL color to RGBA color space.

    Args:
        h (float): The hue component of the color (0-360).
        s (float): The saturation component of the color (0-100).
        l (float): The lightness component of the color (0-100).
        alpha (float, optional): The alpha (opacity) value of the color (0-1). Defaults to 1.

    Returns:
        List[int]: The RGBA representation of the color [r, g, b, alpha].
    """
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return [int(r * 255), int(g * 255), int(b * 255), alpha]


def additive_mix_rgba_colors(base: List[int], added: List[int]) -> List[int]:
    """
    Mixes two RGB colors additively.

    Args:
        base (List[int]): The base color in RGBA format.
        added (List[int]): The color to be added in RGBA format.

    Returns:
        List[int]: The resulting color after the additive mixing in RGBA format.
    """
    alpha_mix = 1 - (1 - added[3]) * (1 - base[3])
    if alpha_mix == 0:
        return [0, 0, 0, 0]
    rgb_mix = [
        round((added[i] * added[3] + base[i] *
              base[3] * (1 - added[3])) / alpha_mix)
        for i in range(3)
    ]
    rgb_mix.append(alpha_mix)
    return rgb_mix


def hsl_mix_rgba_colors(base: List[int], added: List[int]) -> List[int]:
    """
    Mixes two RGB colors using HSL color space.

    Args:
        base (List[int]): The base color in RGBA format.
        added (List[int]): The color to be added in RGBA format.

    Returns:
        List[int]: The resulting color after the HSL mixing in RGBA format.
    """
    hsl1 = rgba_to_hsl(*base)
    hsl2 = rgba_to_hsl(*added)
    mixed_hsl = [
        (hsl1[i] + hsl2[i]) / 2 for i in range(3)
    ] + [1 - (1 - base[3]) * (1 - added[3])]
    return hsl_to_rgba(*mixed_hsl)
