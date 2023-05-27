import random

'''
day 4 
'''

## 🚨 Don't change the code below 👇
#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])
## 🚨 Don't change the code above 👆
#total = 0
#for heihgt in student_heights:
#    total += heihgt
#average = total // len(student_heights)

#print(average)
##Write your code below this row 👇

#------------------------------------------------------------------------------------------------------------------------

'''
the highest score in a class
'''

## 🚨 Don't change the code below 👇
#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
#print(student_scores)
## 🚨 Don't change the code above 👆

#highest_score = student_scores[0]
#for i in range (1, len(student_scores)):
#    if(student_scores[i] > highest_score):
#        highest_score = student_scores[i]

#print(f"The highest score in the class is: {highest_score}")
##Write your code below this row 👇

#--------------------------------------------------------------------------------------------------------------------------

'''
the sum of even numbers from 1 to 100
'''

# total_sum = 0

# for i in range(1, 101):
#     if i%2 == 0:
#         total_sum += i

# print(total_sum)

#--------------------------------------------------------------------------------------------------------------------------

'''
FizzBuzz challenge
'''

# for i in range (1, 101):
#     if i%3 == 0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

#---------------------------------------------------------------------------------------------------------------------------
'''
day 5 project: password generator
'''

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_characters = nr_letters + nr_symbols + nr_numbers
password = ""
index = 0

while total_characters>0:
    if(nr_letters>0 and nr_symbols>0 and nr_numbers>0):
        election = random.randint(0,2)
    elif(nr_letters<=0 and nr_symbols>0 and nr_numbers>0):
        election = random.choice([1,2])
    elif(nr_letters>0 and nr_symbols<=0 and nr_numbers>0):
        election = random.choice([0,2])
    elif(nr_letters>0 and nr_symbols>0 and nr_numbers<=0):
        election = random.choice([0,1])
    elif(nr_letters>0 and nr_symbols<=0 and nr_numbers<=0):
        election = 0
    elif(nr_letters<=0 and nr_symbols>0 and nr_numbers<=0):
        election = 1
    elif(nr_letters<=0 and nr_symbols<=0 and nr_numbers>0):
        election = 2

    #this election is for letters
    if election==0:
        index = random.randint(0, len(letters))
        password += letters[index]
        nr_letters = nr_letters - 1
    #this election is for symbols
    elif election==1:
        index = random.randint(0, len(symbols))
        password += symbols[index]
        nr_symbols = nr_symbols - 1
    #this election is for numbers 
    else:
        index = random.randint(0, len(numbers))
        password += numbers[index]
        nr_numbers = nr_numbers - 1

    total_characters = total_characters -1

print(f"Your new password is: {password}")
