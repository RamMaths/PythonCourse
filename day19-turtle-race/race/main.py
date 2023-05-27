from turtle import Turtle, Screen
from turtle_race import start_poistion, turtle_features, race
import turtle

turtles = {
        "yellow": Turtle(),
        "red": Turtle(),
        "blue": Turtle(),
        "green": Turtle(),
        "orange": Turtle(),
        "purple": Turtle()
        }
screen = Screen()

# screen.screensize(canvwidth=500, canvheight=500)
screen.setup(width=500, height=500)
screen.setworldcoordinates(-500,-500,500,500)

#1.- ask the user for a color
player_wager = screen.textinput("Turtles race", "Select a color: ")
#2.- setting the colors to the turtles
turtle_features(turtles)
#3.- getting to the start position
start_poistion(turtles)
#4.- start the race
winner = race(turtles)

if player_wager == winner:
    print("Ganaste")
else:
    print("Perdiste")

screen.exitonclick()
