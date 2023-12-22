
from utils import echo
import random

arr_star = [
"###~",
"__/^\__",
"\ .★. /",
"/_< >_\\",
"##(~)"
]

decorate = ".:*~*:._"
MAP_TREE = ['*', '&', '¿', '★', 'O']

def draw_base_star(term, x, y):
    for i in range(len(arr_star)):
        string = arr_star[i]
        cantidad = string.count('#')
        string = string.replace('#', '')
        echo(term.move_xy(x - 3 + cantidad, y + i))
        echo(term.on_black(term.yellow(string)))

def draw_tree_trunk(term, x, y, height):
    string = 'MmNmM'
    base = round(height / 5)
    for i in range(base):
        echo(term.move_xy(x - 2, y + 5 + height + i))
        echo(term.on_black(term.lightsalmon4(string)))

tree_positions = []
def draw_base_tree(term, x, y, height):
    for i in range(1, height):
        efecto = random.choice([0, 2])
        pos_x = x - i - round(efecto / 2)
        pos_y = y + 5 + i
        echo(term.move_xy(pos_x, pos_y))
        string = ''
        cantidad = (i * 2 + 1)
        cantidad += efecto
        for j in range(cantidad):
            string += random.choice(MAP_TREE)
        echo(term.on_black(term.forestgreen(string)))
        tree_positions.append([pos_x, pos_y, string])
    draw_tree_trunk(term, x, y, height)