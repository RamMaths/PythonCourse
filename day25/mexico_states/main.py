# pylint: disable=E1101
import pandas
import turtle

#Adding the shape to the turtle then printing the map on the screen
screen = turtle.Screen()
screen.title('Estados de Mexico')
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

#importing the names
states_data = pandas.read_csv('datos.csv')
names_list = states_data['estado'].to_list()
names_dict={}

def get_mouse_click_coor(x, y):
    global name_index
    if name_index < len(names_list):
        name = names_list[name_index]
        names_dict[name] = [x, y]
        print(name, x, y)
        name_index += 1
    else:
        turtle.bye()
        print(names_dict)


# --- main ---

name_index = 0

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

(pandas.DataFrame(names_dict)).to_csv('name_and_coor.csv')
