from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fast')
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.ball_speed = 0
        self.default_ball_speed()
        self.serve()

    def serve(self):
        self.goto(0,0)
        self.direction = random.choice(["First", "Second", "Third", "Fourth"])

    def player_change(self):
        if self.direction=="First":
            self.direction=random.choice(["Third", "Second"])
        elif self.direction=="Second":
            self.direction=random.choice(["First", "Fourth"])
        elif self.direction=="Third":
            self.direction=random.choice(["First", "Fourth"])
        elif self.direction=="Fourth":
            self.direction=random.choice(["Third", "Second"])

    def side_change(self):
        if self.direction=="First":
            self.direction="Fourth"
        elif self.direction=="Second":
            self.direction="Third"
        elif self.direction=="Third":
            self.direction="Second"
        elif self.direction=="Fourth":
            self.direction="First"


    def move(self):
        (x,y) = self.pos()
        if self.direction=="First":
            self.goto(x+self.ball_speed, y+self.ball_speed)
        elif self.direction=="Second":
            self.goto(x-self.ball_speed, y+self.ball_speed)
        elif self.direction=="Third":
            self.goto(x-self.ball_speed, y-self.ball_speed)
        elif self.direction=="Fourth":
            self.goto(x+self.ball_speed, y-self.ball_speed)

    def side_touched(self):
        if self.ycor()>310 or self.ycor()<-310:
            self.side_change()

    def goal(self):
        if self.xcor()>430:
            return "Left"
        elif self.xcor()<-436:
            return "Right"
        else:
            return None

    def increase_ball_speed(self):
        self.ball_speed+=0.012

    def default_ball_speed(self):
        self.ball_speed = 0.125
