from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import ScoreBoard
import time

# creating and setting up the Screen
screen = Screen()

screen.setup(width=900, height=650)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#creating the player object
player1 = Player(1)
player2 = Player(2)
ball = Ball()


#setting up the key bindings
screen.listen()
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")

#settin up the scoreboard
scoreboard = ScoreBoard()

#setting up the winner text
who_wins = Turtle()
who_wins.hideturtle()
who_wins.penup()
who_wins.color("white")

# the game starts ...
counter = 0
still_playing = True
while still_playing==True:
    screen.update()
    ball.move()

    #checking if one of the sides has been touched
    ball.side_touched()

    #checking if anyone has made a goal
    if ball.goal()=="Right":
        player2.increment_score()
        time.sleep(1)
        ball.serve()
        ball.default_ball_speed()
        player1.default_player_speed()
        player2.default_player_speed()
        scoreboard.increment_right_score()
    elif ball.goal()=="Left":
        player1.increment_score()
        time.sleep(1)
        ball.serve()
        ball.default_ball_speed()
        player1.default_player_speed()
        player2.default_player_speed()
        scoreboard.increment_left_score()
    
    #checking if the ball has been hit by a player
    if ball.distance(player1.pos())<48 or ball.distance(player2.pos())<48:
        ball.player_change()

    #increasing the speed to make the game harder
    if counter > 2500:
        ball.increase_ball_speed()
        player1.increment_player_speed()
        player2.increment_player_speed()
        counter = 0

    if player1.score==5:
        winner="Left"
        break
    elif player2.score==5:
        winner="Right"
        break
    counter+=1



# announcing the winner
if winner=="Right":
    who_wins.write(arg="Player 2 wins.", move=False, align="center", font=('Arial', 26, 'normal'))
else:
    who_wins.write(arg="Player 1 wins.", move=False, align="center", font=('Arial', 26, 'normal'))

screen.exitonclick()
