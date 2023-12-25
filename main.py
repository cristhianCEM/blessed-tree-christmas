import blessed
from drawers.map_3d import ConsoleMap3d
from drawers.starsky import draw_starsky
from drawers.moon import draw_full_moon
from drawers.tree import draw_base_star, draw_base_tree, draw_fairy_lights
from drawers.UI import SCENE_DEPTH, draw_message, draw_message_quit


def setup(scene):
    draw_starsky(scene, True)
    draw_full_moon(scene, True)
    draw_base_star(scene, True)
    draw_base_tree(scene, True)
    draw_message(scene)
    draw_message_quit(scene)


def update(scene):
    draw_starsky(scene, False)
    draw_fairy_lights(scene)


def main():
    terminal = blessed.Terminal()
    scene = ConsoleMap3d(terminal, setup, SCENE_DEPTH)
    with terminal.hidden_cursor(), terminal.cbreak(), terminal.location():
        input = None
        while input not in (u'q', u'Q'):
            scene.check_resize()
            update(scene)
            scene.draw()
            input = scene.terminal.inkey(timeout=0.1)


if __name__ == '__main__':
    main()
