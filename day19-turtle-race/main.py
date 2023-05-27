from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_right():
    ##first way-----
    # tim.right(10)
    ##second way----
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_left():
    ##first way----
    # tim.left(10)
    ##second way----
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clear_turtle_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=move_right, key='d')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=clear_turtle_screen, key="c")
screen.listen()

screen.exitonclick()
