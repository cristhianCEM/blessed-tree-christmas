
def additive_mix_RGB_colors(base: list, added: list):
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