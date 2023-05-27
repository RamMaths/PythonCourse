'''
day 9
'''

#Grading program ----------------------------------------------------------------------------------------------------------------

#student_scores = {
#  "Harry": 81,
#  "Ron": 78,
#  "Hermione": 99, 
#  "Draco": 74,
#  "Neville": 62,
#}
## 🚨 Don't change the code above 👆

##TODO-1: Create an empty dictionary called student_grades.

#student_grades = {}

##TODO-2: Write your code below to add the grades to student_grades.👇

#for key in (student_scores):
#    if(student_scores[key]>90 and student_scores[key]<101):
#        student_grades[key] = "Outstanding"
#    elif(student_scores[key]>80 and student_scores[key]<91):
#        student_grades[key] = "Exceeds Exceptations"
#    elif(student_scores[key]>70 and student_scores[key]<81):
#        student_grades[key] = "Acceptable"
#    elif student_scores[key]<70:
#        student_grades[key] = "Fail"
    
#print(student_grades)

## 🚨 Don't change the code below 👇
#print(student_grades)

#Dinctionary in list--------------------------------------------------------------------------------------------------------------

#travel_log = [
#{
#  "country": "France",
#  "visits": 12,
#  "cities": ["Paris", "Lille", "Dijon"]
#},
#{
#  "country": "Germany",
#  "visits": 5,
#  "cities": ["Berlin", "Hamburg", "Stuttgart"]
#},
#]
##🚨 Do NOT change the code above

##TODO: Write the function that will allow new countries
##to be added to the travel_log. 👇

#def add_new_country(country, visits, cities):
#    new_value = {"country": country, "visits": visits, "cities": cities}
#    travel_log.append(new_value)

##🚨 Do not change the code below
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)

#
from screenClear import clear
from art import logo

loop = "yes"
name = ""
bid = 0
bidders = {}
biggest=0

def add_bidder(name, bid):
    bidders[name] = bid

print(logo)
input("Welcome to the secret auction program\n\nEnter to continue...")

while loop=="yes":
    clear()
    name = input("What's your name? ")
    bid = int(input("What's yout bid? "))
    add_bidder(name, bid)

    loop = input("Are there any oders bidders? type 'yes' or 'no'.")

for key in (bidders):
    if bidders[key] > biggest:
        biggest = bidders[key]
        #here i am going to rehuse the variable name to store the name who has the biggest bid
        name = key

clear()
print(f"The winner is {name} with a bid of ${bidders[name]}")
