from turtle import Turtle

X = 420

class Player(Turtle):
    def __init__(self, player_type):
        super().__init__()
        self.penup()
        self.speed('slow')
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=7, stretch_len=2)
        self.player_type = player_type
        self.initial_position()
        self.score = 0
        self.moving_speed=0
        self.default_player_speed()

    
    def default_player_speed(self):
        self.moving_speed=30

    def increment_player_speed(self):
        self.moving_speed+=2

    def initial_position(self):
        if self.player_type==1:
            self.goto(-X-7, 0)
        else: 
            self.goto(X, 0)

    def up(self):
        if self.ycor()>250:
            pass
        else:
            y = self.ycor()
            if self.player_type==1:
                self.goto(-X-7, y+self.moving_speed)
            else: 
                self.goto(X, y+self.moving_speed)

    def down(self):
        if self.ycor()<-240:
            pass
        else:
            y = self.ycor()
            if self.player_type==1:
                self.goto(-X-7, y-self.moving_speed)
            else: 
                self.goto(X, y-self.moving_speed)

    def increment_score(self):
        self.score+=1
