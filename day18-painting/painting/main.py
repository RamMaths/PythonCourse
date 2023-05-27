# pylint: disable=E1101
import random
import colorgram
import turtle as turtle_module

def random_color():
    rgb_colors =[(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111)]
    return random.choice(rgb_colors)

turtle_module.colormode(255)

#creating a Turtle object
tim = turtle_module.Turtle()

def get_coordinates(start):
    beginning = start * (-1)
    ending =  start
    step = start // 5
    
    return(beginning, ending, step)

(beginning, ending, step) = get_coordinates(350)

for i in range(beginning, ending, step):
    for j in range(beginning, ending, step):
        tim.penup()
        tim.goto(j,i)
        tim.pendown()
        tim.dot(30, random_color())


#avoid exiting if we don't want
screen = turtle_module.Screen()
screen.exitonclick()
