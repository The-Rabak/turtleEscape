import argparse
import inspect
import turtle
import pickle
import random
import draw_bag
from CommandArgs import CommandArgs
from parseargs import ParseArgs


def escaped(position):
    x = position[0]
    y = position[1]

    return x < -35 or x > 35 or y < -35 or y > 35


def draw_line(angle=0, step=5):
    t = turtle.Turtle()
    while not escaped(t.position()):
        t.left(angle)
        t.forward(step)


def store_position_data(L, t):
    position = t.position()
    L.append([position[0], position[1], escaped(position)])


def draw_square(t, size):
    L = []
    for i in range(4):
        t.forward(size)
        t.left(90)
        store_position_data(L, t)
    return L


def draw_squares(number):
    t = turtle.Turtle()
    L = []

    for i in range(1, number + 1):
        t.penup()
        t.goto(-i, -i)
        t.pendown()
        L.extend(draw_square(t, i * 2))

    return L


def draw_squares_til_escape(n):
    t = turtle.Turtle()
    L = draw_squares(n)
    with open('squares_dat', "wb") as f:
        pickle.dump(L, f)


def draw_spirangles(n):
    t = turtle.Turtle()
    for i in range(1, n):
        t.forward(i * 10)
        t.right(120)


def draw_rand_spirangles_until_escaped():
    t = turtle.Turtle()
    t.left(random.randint(0, 360))
    t.pendown()

    i = 0
    turn = 360 / random.randint(1, 10)
    L = []
    store_position_data(L, t)

    while not escaped(t.position()):
        i += 1
        t.forward(i * 5)
        t.right(turn)
        store_position_data(L, t)
    return L


def draw_random_spirangles():
    L = []
    for i in range(2):
        L.extend(draw_rand_spirangles_until_escaped())

    # with open("data_rand", "wb") as f:
    #     #pickle.dump(L, f)
    return True


def get_fn_dict():
    return {"line": draw_line, "squares": draw_squares_til_escape, "spirangles": draw_random_spirangles}

def set_args(input_args):
    parser = argparse.ArgumentParser()
    for arg in input_args:
        if not isinstance(arg, CommandArgs):
            continue
        print(arg.get_choices())

    return parser.parse_args()

if __name__ == '__main__':
    fns = get_fn_dict()
    fn_arg = CommandArgs(["-f", "--function"], str, choices = fns, help="one of " + ", ".join(fns.keys()))
    num_arg = CommandArgs(["-n"], int, default=50, help="how many?")
    argsParser = ParseArgs([fn_arg, num_arg])
    argsParser.set_args()
    args = argsParser.get_args()
    #
    # fns = {"line": draw_line,
    #        "squares": draw_squares_til_escape,
    #        "spirangles": draw_random_spirangles}
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-f", "--function",
    #                     choices=fns,
    #                     default='spirangles',
    #                     help="One of " + ', '.join(fns.keys()))
    # parser.add_argument("-n", "--number",
    #                     default=50,
    #                     type=int, help="How many?")
    # args = parser.parse_args()
    try:
        f = fns[args.function]
        turtle.setworldcoordinates(-70., -70., 70., 70.)
        draw_bag.draw_bag()
        turtle.hideturtle()
        if len(inspect.getfullargspec(f).args) == 1:
            f(int(args.n))
        else:
            f()
        turtle.getscreen().destroy()
    except KeyError:
        argsParser.get_parser_help()
