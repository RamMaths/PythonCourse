from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from high_score import HighScore

# setting up the window
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")

highscore = HighScore()

play_again = "yes"
while play_again == "yes":
    food = Food()
    scoreboard = ScoreBoard()
    snake = Snake()
    highscore.check_new_highscore(scoreboard.score)

    screen_sleep = 0.045
    still_playing = True
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    while still_playing:
        screen.update()
        time.sleep(screen_sleep)
        snake.move()
        
        # detecting collision with the food
        if snake.head.distance(food.position) < 10:
            food.refresh()
            snake.add_segment()
            scoreboard.increment_score()
            screen_sleep -= 0.0005

        if snake.wall_collision() == False or snake.tail_collision() == False:
            break

    highscore.check_new_highscore(scoreboard.score)

    play_again = screen.textinput("Game over", "Type 'yes' to play_again: ")
    scoreboard.clear()
    highscore.clear()
    food.clear_food()
    snake.clear_snake()
