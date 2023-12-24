import colorsys
from typing import List
from math import ceil


def promedio(a: float, b: float) -> float:
    """
    Devuelve el promedio entre dos números.
    """
    return (a + b) / 2


def combine_alpha(alpha1: float, alpha2: float) -> float:
    """
    Devuelve el alpha resultante de la mezcla de dos colores.
    """
    return 1 - (1 - alpha1) * (1 - alpha2)


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
    return [ceil(r * 255), ceil(g * 255), ceil(b * 255), alpha]


def additive_mix_rgba_colors(base: List[int], added: List[int]) -> List[int]:
    """
    Mixes two RGB colors additively.

    Args:
        base (List[int]): The base color in RGBA format.
        added (List[int]): The color to be added in RGBA format.

    Returns:
        List[int]: The resulting color after the additive mixing in RGBA format.
    """
    alpha_mix = combine_alpha(added[3], base[3])
    if alpha_mix == 0:
        return [0, 0, 0, 0]
    rgb_mix = [
        round((added[i] * added[3] + base[i] *
              base[3] * (1 - added[3])) / alpha_mix)
        for i in range(3)
    ]
    rgb_mix.append(alpha_mix)
    return rgb_mix


def hsl_mix_rgba_colors(color1: List[int], color2: List[int]) -> List[int]:
    """
    Mixes two RGB colors using HSL color space.

    Args:
        color1 (List[int]): The color1 in RGBA format.
        color2 (List[int]): The color2 in RGBA format.

    Returns:
        List[int]: The resulting color after the HSL mixing in RGBA format.
    """
    hsl1 = rgba_to_hsl(*color1)
    hsl2 = rgba_to_hsl(*color2)
    alpha1 = color1[3] or 1
    alpha2 = color2[3] or 1
    mixed_hsl = [
        promedio(hsl1[i], hsl2[i]) for i in range(3)
    ]
    mixed_hsl.append(combine_alpha(alpha1, alpha2))
    # Ajusta el matiz si la diferencia es mayor a 180 grados
    if abs(hsl1[0] - hsl2[0]) > 180:
        mixed_hsl[0] = (mixed_hsl[0] + 180) % 360
    return hsl_to_rgba(*mixed_hsl)
