import blessed
import random
import math
import time

from utils import echo, get_text_formatted
from drawers.starsky import draw_starsky
from drawers.moon import draw_translate_moon
from drawers.tree import draw_base_star, draw_base_tree

MAP_COLOR = ['aliceblue', 'antiquewhite', 'antiquewhite1', 'antiquewhite2', 'antiquewhite3', 'antiquewhite4', 'aqua', 'aquamarine', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'beige', 'bisque', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanchedalmond', 'blue', 'blue2', 'blue3', 'blue4', 'blueviolet', 'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadetblue', 'cadetblue1', 'cadetblue2', 'cadetblue3', 'cadetblue4', 'chartreuse', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflowerblue', 'crimson', 'cyan2', 'cyan3', 'cyan4', 'darkgoldenrod', 'darkgoldenrod1', 'darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3', 'darkolivegreen4', 'darkorange', 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4', 'darkorchid', 'darkorchid1', 'darkorchid2', 'darkorchid3', 'darkorchid4', 'darkred', 'darksalmon', 'darkseagreen', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3', 'darkseagreen4', 'darkslateblue', 'darkturquoise', 'darkviolet', 'deeppink', 'deeppink2', 'deeppink3', 'deeppink4', 'deepskyblue', 'deepskyblue2', 'deepskyblue3', 'deepskyblue4', 'dodgerblue', 'dodgerblue2', 'dodgerblue3', 'dodgerblue4', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'green', 'green2', 'green3', 'green4', 'greenyellow', 'honeydew', 'honeydew2', 'honeydew3', 'honeydew4', 'hotpink', 'hotpink1', 'hotpink2', 'hotpink3', 'hotpink4', 'indianred', 'indianred1', 'indianred2', 'indianred3', 'indianred4', 'indigo', 'ivory', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavenderblush', 'lavenderblush2', 'lavenderblush3', 'lavenderblush4', 'lawngreen', 'lemonchiffon', 'lemonchiffon2', 'lemonchiffon3', 'lemonchiffon4', 'lightblue', 'lightblue1', 'lightblue2', 'lightblue3', 'lightblue4', 'lightcoral', 'lightcyan', 'lightcyan2', 'lightcyan3', 'lightcyan4', 'lightgoldenrod', 'lightgoldenrod1', 'lightgoldenrod2', 'lightgoldenrod3', 'lightgoldenrod4', 'lightgoldenrodyellow', 'lightgreen', 'lightpink', 'lightpink1', 'lightpink2', 'lightpink3', 'lightpink4', 'lightsalmon', 'lightsalmon2',
             'lightsalmon3', 'lightsalmon4', 'lightseagreen', 'lightskyblue', 'lightskyblue1', 'lightskyblue2', 'lightskyblue3', 'lightskyblue4', 'lightslateblue', 'lightsteelblue', 'lightsteelblue1', 'lightsteelblue2', 'lightsteelblue3', 'lightsteelblue4', 'lightyellow', 'lightyellow2', 'lightyellow3', 'lightyellow4', 'limegreen', 'linen', 'magenta2', 'magenta3', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'mediumorchid', 'mediumorchid1', 'mediumorchid2', 'mediumorchid3', 'mediumorchid4', 'mediumpurple', 'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'moccasin', 'navajowhite', 'navajowhite2', 'navajowhite3', 'navajowhite4', 'navy', 'oldlace', 'olive', 'olivedrab', 'olivedrab1', 'olivedrab2', 'olivedrab3', 'olivedrab4', 'orange', 'orange2', 'orange3', 'orange4', 'orangered', 'orangered2', 'orangered3', 'orangered4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'palegoldenrod', 'palegreen', 'palegreen1', 'palegreen3', 'palegreen4', 'paleturquoise', 'paleturquoise1', 'paleturquoise2', 'paleturquoise3', 'paleturquoise4', 'papayawhip', 'peachpuff', 'peachpuff2', 'peachpuff3', 'peachpuff4', 'peru', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powderblue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'rebeccapurple', 'red', 'red2', 'red3', 'rosybrown', 'rosybrown1', 'rosybrown2', 'rosybrown3', 'rosybrown4', 'royalblue', 'royalblue1', 'royalblue2', 'royalblue3', 'royalblue4', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandybrown', 'seagreen', 'seagreen1', 'seagreen2', 'seagreen3', 'seashell', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'silver', 'skyblue', 'skyblue1', 'skyblue2', 'skyblue3', 'skyblue4', 'slateblue', 'slateblue1', 'slateblue2', 'slateblue3', 'slateblue4', 'snow', 'snow2', 'snow3', 'snow4', 'springgreen', 'springgreen2', 'springgreen3', 'springgreen4', 'steelblue', 'steelblue1', 'steelblue2', 'steelblue3', 'steelblue4', 'tan', 'tan1', 'tan2', 'tan4', 'teal', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'tomato', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet', 'violetred', 'violetred1', 'violetred2', 'violetred3', 'violetred4', 'webgreen', 'webmaroon', 'webpurple', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'yellow', 'yellow2', 'yellow3', 'yellow4']
MESSAGE = 'Feliz Navidad!'
MESSAGE_FONT = 'slscript'
MESSAGE_HEIGHT = 5
MESSAGE_QUIT = 'Press Q to quit.'
LEN_MESSAGE_QUIT = len(MESSAGE_QUIT)


def draw_message_quit(terminal):
    echo(terminal.move_yx(terminal.height, terminal.width - LEN_MESSAGE_QUIT))
    echo(terminal.bright_black(MESSAGE_QUIT))


def draw_message(terminal):
    echo(terminal.move_yx(terminal.height - MESSAGE_HEIGHT, 0))
    echo(terminal.red(get_text_formatted(MESSAGE, font=MESSAGE_FONT)))


def setup(terminal):
    echo(terminal.on_black(terminal.clear()))
    echo(terminal.move_xy(0, 0))
    draw_starsky(terminal, True)
    draw_translate_moon(terminal, True)
    star_x = math.floor(terminal.width / 2)
    star_y = 1
    draw_base_star(terminal, star_x, star_y)
    tree_x = math.floor(terminal.width / 2)
    tree_y = 0
    tree_height = terminal.height - 10
    draw_base_tree(terminal, tree_x, tree_y, tree_height)
    draw_message(terminal)
    draw_message_quit(terminal)


def loop(terminal):
    draw_starsky(terminal, False)
    draw_translate_moon(terminal, False)


def main():
    terminal = blessed.Terminal()
    with terminal.hidden_cursor(), terminal.cbreak(), terminal.location():
        current_width, current_height = terminal.width, terminal.height
        setup(terminal)
        input = None
        while input not in (u'q', u'Q'):
            width, height = terminal.width, terminal.height
            if current_width != width or current_height != height:
                current_width, current_height = width, height
                setup(terminal)
            else:
                loop(terminal)
            input = terminal.inkey(timeout=0.1)
    exit()
    # for i in range(len(tree_positions)):
    #     pos_x = tree_positions[i][0]
    #     pos_y = tree_positions[i][1]
    #     string = tree_positions[i][2]
    #     new_string = ''
    #     for str in string:
    #         if str == 'O':
    #             color_random = random.choice(MAP_COLOR)
    #             new_string += getattr(terminal, color_random)('O')
    #         else:
    #             new_string += terminal.forestgreen(str)
    #     echo(terminal.move_xy(pos_x, pos_y))
    #     echo(terminal.on_black(new_string))


if __name__ == '__main__':
    main()
