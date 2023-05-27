from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=263)
        self.score = 0
        self.write(arg=f"Score: {self.score}", move=False,  align="center", font=('Arial', 20, 'normal'))

    def increment_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False,  align="center", font=('Arial', 20, 'normal'))
