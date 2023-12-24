import colorsys


def rgba_to_hsl(rgba):
    r, g, b, a = rgba
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return [h * 360, s * 100, l * 100, a]


def hsl_to_rgba(hsl):
    h, s, l, a = hsl
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return [int(r * 255), int(g * 255), int(b * 255), a]


def additive_mix_rgba_colors(base: list, added: list):
    """
        Mezcla dos colores RGB de forma aditiva
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


def hsl_mix_rgba_colors(color1: list, color2: list):
    hsl1 = rgba_to_hsl(color1)
    hsl2 = rgba_to_hsl(color2)
    mixed_hsl = [
        (hsl1[i] + hsl2[i]) / 2 for i in range(3)
    ] + [1 - (1 - color1[3]) * (1 - color2[3])]  # mezcla de alfa
    return hsl_to_rgba(mixed_hsl)
