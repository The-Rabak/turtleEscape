import turtle

def draw_bag():
    turtle.shape('turtle')
    turtle.pen(pencolor='brown', pensize=5)
    turtle.penup()

    turtle.goto((-35, 35))
    turtle.pendown()
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
