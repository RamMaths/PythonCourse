from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        self.position = self.pos()
        self.clear()

    def refresh(self):
        random_x = random.randint(-280,260)
        random_y = random.randint(-280,260)
        location = (random_x, random_y)
        self.position = location
        self.goto(location)

    def clear_food(self):
        self.goto(1000,10000)


