# pylint: disable=E1101
import pandas
import turtle
import csv

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#importing the satates and its location
states = pandas.read_csv('50_states.csv')
# --- main ---

correct_answers = []
while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States correct", prompt="What's another state's name you know?")
    answer_state = answer_state.title()
    if answer_state in states.values:
        #setting up the turtle
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_turtle.color('black')

        #locating the actual row then using its coordinates
        actual_row = states.loc[states.state==answer_state]
        answer_turtle.goto(int(actual_row.x),int(actual_row.y))
        answer_turtle.write(answer_state)
        correct_answers.append(answer_state)
    elif answer_state=='Exit':
        break

states_to_learn = [state for state in states.state if state not in correct_answers]

print("The states you must review are: ")
for state in states_to_learn:
    print(state)

(pandas.DataFrame(states_to_learn, columns=['states'])).to_csv('states_to_learn.csv', index=False)
