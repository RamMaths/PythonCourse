from turtle import Turtle

class HighScore(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=-280)
        with open("highscore.txt") as file:
            self.highscore = file.read()
        self.write(arg=f"High score: {self.highscore}", move=False,  align="center", font=('Arial', 20, 'normal'))


    def check_new_highscore(self, actual_score):
        if actual_score>int(self.highscore):
            self.highscore=actual_score
            with open("highscore.txt", mode="w") as file:
                file.truncate(0)
                file.write(str(self.highscore))
            self.clear()
            self.write(arg=f"High score: {self.highscore}", move=False,  align="center", font=('Arial', 20, 'normal'))
        else: 
            self.write(arg=f"High score: {self.highscore}", move=False,  align="center", font=('Arial', 20, 'normal'))


