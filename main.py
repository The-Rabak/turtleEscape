import turtle
import pickle
import random
import draw_bag

def escaped(position):
    x = position[0]
    y = position[1]

    return x < -35 or x > 35 or y < -35 or y > 35

def draw_line(angle = 0, step = 5): 
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
    turn = 360 / random.randint(0, 10)
    L = []
    store_position_data(L, t)
    
    while not escaped(t.position()):
        i += 1
        t.forward(i * 5)
        t.right(turn)
        store_position_data(L, t)
    return L

def draw_random_spirangels():
    L = []
    for i in range(10):
        L.extend(draw_rand_spirangles_until_escaped())
    with open("spirangles_dat", "wb") as f:
        pickle.dump(L, f)

if __name__ == '__main__':
    turtle.setworldcoordinates(-70., -70., 70., 70.)
    draw_bag.draw_bag()
    turtle.mainloop()
    
