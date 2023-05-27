# pylint: disable=E1101
import turtle
import random

timmy = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)
screen.tracer(True)
timmy.shape("turtle")
timmy.speed("normal")

colors = ["maroon", "red", "yellow", "green", "medium turquoise", "teal", "medium blue", "dark salmon", "dark orchid", "indian red", "dark orange", "dark olive green", "bisque", "slate gray"]

def give_direction():
    return random.choice([0, 90, 180, 270])

def give_distance():
    return random.randint(40, 100)

def give_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)

def draw_shape(sides):
    counter=0
    while counter<sides:
        screen.delay(300)
        angle = 360/sides
        timmy.forward(100)
        timmy.right(angle)
        counter+=1

def draw_spirograph(gap_size):
    for i in range(360//gap_size):
        timmy.speed("fastest")
        timmy.color(give_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)
    pass
# for i in range(100):
    #random way turtle----------------------------------------------
    # timmy.speed("fastest")
    # screen.delay(300)
    # timmy.pensize(15)
    # timmy.color(give_color())
    # timmy.right(give_direction())
    # timmy.forward(give_distance())

draw_spirograph(5)


screen.exitonclick()
