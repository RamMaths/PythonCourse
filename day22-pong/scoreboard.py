from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=263)
        self.left_score = 0
        self.right_score = 0
        self.write(arg=f"Score: {self.left_score} \t\t\tScore: {self.right_score}", move=False,  align="center", font=('Arial', 20, 'normal'))

    def increment_left_score(self):
        self.left_score+=1
        self.clear()
        self.write(arg=f"Score: {self.left_score} \t\t\tScore: {self.right_score}", move=False,  align="center", font=('Arial', 20, 'normal'))

    def increment_right_score(self):
        self.right_score+=1
        self.clear()
        self.write(arg=f"Score: {self.left_score} \t\t\tScore: {self.right_score}", move=False,  align="center", font=('Arial', 20, 'normal'))
