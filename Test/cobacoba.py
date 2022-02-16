import turtle

turtle.bgcolor("white")
turtle.width(12)
turtle.speed(10)


def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


def hati():
    turtle.color("red", "red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(112)
    turtle.end_fill()


hati()
turtle.pencolor("white")
turtle.penup()
turtle.goto(0, 170)
turtle.pendown()

for zigzag in range(3):
    turtle.left(75)
    turtle.forward(40)
    turtle.right(65)
    turtle.forward(40)

turtle.done()
