import random
import math

TREE_DEPTH = 2
STAR = [
    "###,",
    "__/^\__",
    "\ .★. /",
    "/_< >_\\",
    "##(~)"
]
STAR_COLOR = (255, 255, 0, 1)
TRUNK_COLOR = (255, 160, 122, 1)
TREE_COLOR = (34, 139, 34, 0.5)
MAP_TREE = ['*', '&', '¿', '★', 'O']
MAP_TRUNK = ['M', 'm', 'N', 'n', '@']
star_x = 0
star_y = 0
tree_positions = []
decorate = ".:*~*:._"


def draw_base_star(scene, reset: bool = False):
    global star_x, star_y
    if (reset):
        star_x = math.floor(scene.width / 2)
        star_y = 1
    for i in range(len(STAR)):
        string = STAR[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        tmp_x = star_x - 3 + cantidad
        tmp_y = star_y + i
        scene.set_message(tmp_x, tmp_y, TREE_DEPTH, string, STAR_COLOR)


def draw_tree_trunk(scene, x, y, height):
    base = round(height / 5)
    for i in range(base):
        string = ''.join([random.choice(MAP_TRUNK) for _ in range(5)])
        tmp_x = x - 2
        tmp_y = y + 5 + height + i
        scene.set_message(tmp_x, tmp_y, TREE_DEPTH, string, TRUNK_COLOR)


def draw_base_tree(scene, reset: bool = False):
    global tree_positions
    if (reset):
        tree_positions = []
    tree_x = math.floor(scene.width / 2)
    tree_y = 0
    tree_height = scene.height - 10
    for i in range(1, tree_height):
        efecto = random.choice([0, 2])
        pos_x = tree_x - i - round(efecto / 2)
        pos_y = tree_y + 5 + i
        string = ''
        cantidad = (i * 2 + 1)
        cantidad += efecto
        for _ in range(cantidad):
            string += random.choice(MAP_TREE)
        scene.set_message(pos_x, pos_y, TREE_DEPTH, string, TREE_COLOR)
        tree_positions.append([pos_x, pos_y, string])
    draw_tree_trunk(scene, tree_x, tree_y, tree_height)


def random_color(alpha: float = 1):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha)


def draw_fairy_lights(scene):
    global tree_positions
    for item in tree_positions:
        ini_x = item[0]
        ini_y = item[1]
        string = item[2]
        for x, caracter in enumerate(string):
            if caracter == 'O':
                color = random_color()
                scene.set_point(ini_x + x, ini_y, TREE_DEPTH, caracter, color)
