import random

def start_poistion(turtles):
    counter = -2
    for timmy in turtles:
        turtles[timmy].penup()
        turtles[timmy].goto(-500, (125*counter))
        counter+=1

def turtle_features(turtles):
    for timmy in turtles:
        turtles[timmy].shape('turtle')
        turtles[timmy].color(timmy)

def race(turtles):
    still_on_the_way = True
    while still_on_the_way==True:
        for timmy in turtles:
            turtles[timmy].speed('fastest')
            length = random.randint(10, 35)
            distance = check_limit(length, turtles[timmy])
            turtles[timmy].fd(distance)
            still_on_the_way = finish_line(turtles[timmy])
            if still_on_the_way==False:
                return timmy

def check_limit(distance, turtle_object):
    (x,y) = turtle_object.pos()
    current_distnace = x + distance
    if current_distnace>500:
        new_distnace = 500 - current_distnace 
        return distance + new_distnace
    else:
        return distance

def finish_line(turtle_object):
    (x,y) = turtle_object.pos()
    if (x == 500):
        return False
    else:
        return True

