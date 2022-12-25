from functools import partial
import blessed
import random
import math
import time
import pyfiglet
## draw a tree with lights that blink in diferent colors with blessed
# python 2/3 compatibility, provide 'echo' function as an
# alias for "print without newline and flush"
try:
    # pylint: disable=invalid-name
    #         Invalid constant name "echo"
    echo = partial(print, end='', flush=True)
    echo(u'')
except TypeError:
    # TypeError: 'flush' is an invalid keyword argument for this function
    import sys

    def echo(text):
        """Python 2 version of print(end='', flush=True)."""
        sys.stdout.write(u'{0}'.format(text))
        sys.stdout.flush()

arr_star = [
    "###ʌ",
    "##/|\ ",
    "< -+- >",
    "##\|/",
    "###v",
    "###X"
]

arr_moon_middle = [
"#########___---___",
"######.-'         '-.",
"####./   ()      .-. \.",
"###/   o    .   (   )  \  ",
"##/ .            '-'    \ ",
"#| ()    .  O         .  |",
"|                         |",
"|    o           ()       |",
"|       .--.          O   |",
"#| .   |    |            |",
"##\    `.__.'    o   .  /",
"###\                   /",
"####`\  o    ()      /'",
"######`--_       _--'",
"######### ''---''"
]

# draw sky
def draw_sky(term, width, height):
    term.move_xy(0, 0)
    for y in range(height):
        for x in range(width):
            # draw stars white character * on the sky
            if random.randint(0, 100) > 99:
                echo(term.on_black(term.bright_white('*')))
            else:
                echo(term.on_black(term.bright_white(' ')))

def draw_base_moon(term, x, y):
    for i in range(len(arr_moon_middle)):
        string = arr_moon_middle[i]
        # count # in the string
        cantidad = string.count('#')
        # replace # by space
        string = string.replace('#', '')
        echo(term.move_xy(x + cantidad, y + i))
        echo(term.on_black(term.bright_white(string)))

def draw_base_star(term, x, y):
    # draw star on the tree
    for i in range(len(arr_star)):
        string = arr_star[i]
        # count # in the string
        cantidad = string.count('#')
        # replace # by space
        string = string.replace('#', '')
        echo(term.move_xy(x - 3 + cantidad, y + i))
        echo(term.on_black(term.yellow(string)))

tree_positions = []
def draw_base_tree(term, x, y, height):
    random_string = ['*', '&', '¿', '*', 'O']
    # draw tree with for loop
    for i in range(1, height):
        efecto = random.choice([0, 2])
        pos_x = x - i - round(efecto / 2)
        pos_y = y + 5 + i
        echo(term.move_xy(pos_x, pos_y))
        string = ''
        cantidad = (i * 2 + 1)
        cantidad += efecto
        for j in range(cantidad):
            string += random.choice(random_string)
        echo(term.on_black(term.forestgreen(string)))
        tree_positions.append([pos_x, pos_y, string])
    # draw tree trunk
    string = 'MmNmM'
    base = round(height / 5)
    for i in range(base):
        echo(term.move_xy(x - 2, y + 5 + height + i))
        echo(term.on_black(term.lightsalmon4(string)))

map_colors = ['aliceblue','antiquewhite','antiquewhite1','antiquewhite2','antiquewhite3','antiquewhite4','aqua','aquamarine','aquamarine2','aquamarine3','aquamarine4','beige','bisque','bisque2','bisque3','bisque4','black','blanchedalmond','blue','blue2','blue3','blue4','blueviolet','brown','brown1','brown2','brown3','brown4','burlywood','burlywood1','burlywood2','burlywood3','burlywood4','cadetblue','cadetblue1','cadetblue2','cadetblue3','cadetblue4','chartreuse','chartreuse2','chartreuse3','chartreuse4','chocolate','chocolate1','chocolate2','chocolate3','chocolate4','coral','coral1','coral2','coral3','coral4','cornflowerblue','crimson','cyan2','cyan3','cyan4','darkgoldenrod','darkgoldenrod1','darkgoldenrod2','darkgoldenrod3','darkgoldenrod4','darkgreen','darkkhaki','darkmagenta','darkolivegreen','darkolivegreen1','darkolivegreen2','darkolivegreen3','darkolivegreen4','darkorange','darkorange1','darkorange2','darkorange3','darkorange4','darkorchid','darkorchid1','darkorchid2','darkorchid3','darkorchid4','darkred','darksalmon','darkseagreen','darkseagreen1','darkseagreen2','darkseagreen3','darkseagreen4','darkslateblue','darkturquoise','darkviolet','deeppink','deeppink2','deeppink3','deeppink4','deepskyblue','deepskyblue2','deepskyblue3','deepskyblue4','dodgerblue','dodgerblue2','dodgerblue3','dodgerblue4','firebrick','firebrick1','firebrick2','firebrick3','firebrick4','floralwhite','forestgreen','fuchsia','gainsboro','ghostwhite','gold','gold2','gold3','gold4','goldenrod','goldenrod1','goldenrod2','goldenrod3','goldenrod4','green','green2','green3','green4','greenyellow','honeydew','honeydew2','honeydew3','honeydew4','hotpink','hotpink1','hotpink2','hotpink3','hotpink4','indianred','indianred1','indianred2','indianred3','indianred4','indigo','ivory','ivory2','ivory3','ivory4','khaki','khaki1','khaki2','khaki3','khaki4','lavender','lavenderblush','lavenderblush2','lavenderblush3','lavenderblush4','lawngreen','lemonchiffon','lemonchiffon2','lemonchiffon3','lemonchiffon4','lightblue','lightblue1','lightblue2','lightblue3','lightblue4','lightcoral','lightcyan','lightcyan2','lightcyan3','lightcyan4','lightgoldenrod','lightgoldenrod1','lightgoldenrod2','lightgoldenrod3','lightgoldenrod4','lightgoldenrodyellow','lightgreen','lightpink','lightpink1','lightpink2','lightpink3','lightpink4','lightsalmon','lightsalmon2','lightsalmon3','lightsalmon4','lightseagreen','lightskyblue','lightskyblue1','lightskyblue2','lightskyblue3','lightskyblue4','lightslateblue','lightsteelblue','lightsteelblue1','lightsteelblue2','lightsteelblue3','lightsteelblue4','lightyellow','lightyellow2','lightyellow3','lightyellow4','limegreen','linen','magenta2','magenta3','maroon','maroon1','maroon2','maroon3','maroon4','mediumorchid','mediumorchid1','mediumorchid2','mediumorchid3','mediumorchid4','mediumpurple','mediumpurple1','mediumpurple2','mediumpurple3','mediumpurple4','mediumseagreen','mediumslateblue','mediumspringgreen','mediumturquoise','mediumvioletred','midnightblue','mintcream','moccasin','navajowhite','navajowhite2','navajowhite3','navajowhite4','navy','oldlace','olive','olivedrab','olivedrab1','olivedrab2','olivedrab3','olivedrab4','orange','orange2','orange3','orange4','orangered','orangered2','orangered3','orangered4','orchid','orchid1','orchid2','orchid3','orchid4','palegoldenrod','palegreen','palegreen1','palegreen3','palegreen4','paleturquoise','paleturquoise1','paleturquoise2','paleturquoise3','paleturquoise4','papayawhip','peachpuff','peachpuff2','peachpuff3','peachpuff4','peru','pink','pink1','pink2','pink3','pink4','plum','plum1','plum2','plum3','plum4','powderblue','purple','purple1','purple2','purple3','purple4','rebeccapurple','red','red2','red3','rosybrown','rosybrown1','rosybrown2','rosybrown3','rosybrown4','royalblue','royalblue1','royalblue2','royalblue3','royalblue4','salmon','salmon1','salmon2','salmon3','salmon4','sandybrown','seagreen','seagreen1','seagreen2','seagreen3','seashell','seashell2','seashell3','seashell4','sienna','sienna1','sienna2','sienna3','sienna4','silver','skyblue','skyblue1','skyblue2','skyblue3','skyblue4','slateblue','slateblue1','slateblue2','slateblue3','slateblue4','snow','snow2','snow3','snow4','springgreen','springgreen2','springgreen3','springgreen4','steelblue','steelblue1','steelblue2','steelblue3','steelblue4','tan','tan1','tan2','tan4','teal','thistle','thistle1','thistle2','thistle3','tomato','tomato2','tomato3','tomato4','turquoise','turquoise1','turquoise2','turquoise3','turquoise4','violet','violetred','violetred1','violetred2','violetred3','violetred4','webgreen','webmaroon','webpurple','wheat','wheat1','wheat2','wheat3','wheat4','yellow','yellow2','yellow3','yellow4']

def main():
    term = blessed.Terminal()
    width, height = term.width, term.height
    # poner por defecto el color midnightblue
    echo(term.on_black(term.clear()))
    draw_sky(term, width, height)
    moon_x = math.floor(width / 10)
    moon_y = math.floor(height / 9)
    draw_base_moon(term, moon_x, moon_y)
    star_x = math.floor(width / 2)
    star_y = 1
    draw_base_star(term, star_x, star_y)
    tree_x = math.floor(width / 2)
    tree_y = star_y
    draw_base_tree(term, tree_x, tree_y, 25)
    inp = None

    echo(term.move_yx(term.height - 5, 3))
    text = pyfiglet.figlet_format("Feliz Navidad!", font = "smkeyboard" )
    echo(term.red(text))
    echo(term.move_yx(term.height, 0))
    echo(term.bright_black('Press Q to quit.'))
    echo(term.move_yx(0, 0))
    with term.hidden_cursor(), term.cbreak(), term.location():
        while inp not in (u'q', u'Q'):
            inp = term.inkey(timeout=1)
            # draw tree with for loop with tree_positions
            for i in range(len(tree_positions)):
                pos_x = tree_positions[i][0]
                pos_y = tree_positions[i][1]
                string = tree_positions[i][2]
                new_string = ''
                for str in string:
                    # put color random a caracter O
                    if str == 'O':
                        color_random = random.choice(map_colors)
                        new_string += getattr(term, color_random)('O')
                    else:
                        new_string += term.forestgreen(str)
                echo(term.move_xy(pos_x, pos_y))
                echo(term.on_black(new_string))
            time.sleep(0.5)

if __name__ == '__main__':
    main()