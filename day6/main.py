'''
day 6
'''
#Hurdles loop challenge------------------------------------------------

# this challenge is in this web https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jumping_obstacle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for i in range(6):
#     jumping_obstacle()

#----------------------------------------------------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def relocate():
    while(wall_in_front()==True or front_is_clear()==False or wall_on_right==False):
        turn_left()

def obstacle():
    relocate()
    while wall_on_right()==True and wall_in_front()==False:
        move()


while at_goal() == False:
    if right_is_clear()==True:
            turn_right()
            
    if wall_in_front()==True and front_is_clear()==False:
        obstacle()
    else:        
        move()

