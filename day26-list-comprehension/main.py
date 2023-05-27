umbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
## 🚨 Do Not Change the code above

##Write your 1 line code 👇 below:

#def odd(number):
#    condition = False
#    for i in range(2, 10):
#        if number%i==0 and number!=i:
#            condition=False
#            break
#        else:
#            condition=True

#    return condition

#result = [number for number in numbers if odd(number)==True]

##Write your code 👆 above:

#print(result)

# # --------

# with open('file1.txt') as file1:
#     file1_data = file1.readlines()
# with open('file2.txt') as file2:
#     file2_data = file2.readlines()

# result = [int(number) for number in file1_data if number in file2_data] 
# print(result)

# # Write your code above 👆

# print(result)

#--===---===--===--===--=== DICTIONARY COMPREHENSION --===---===--===--===--===

# import random 

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# students_scores = {student:random.randint(1,101) for student in names}

# student_have_approved = {key:value for(key,value) in students_scores.items() if value>=70}

# print(students_scores)


## EXCERSISE 1   

#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
## Don't change code above 👆

## Write your code below:
#words_in_sentence = sentence.split()
#letters_in_words = {key:len(key) for key in words_in_sentence}

##Another option
## letters_in_words = {key:len(key) for key in sentence.split()}

#print(letters_in_words)

##EXCERSISE 2

#weather_c = {
#    "Monday": 12,
#    "Tuesday": 14,
#    "Wednesday": 15,
#    "Thursday": 14,
#    "Friday": 21,
#    "Saturday": 22,
#    "Sunday": 24,
#}
## 🚨 Don't change code above 👆

## Write your code 👇 below:

#weather_f = { day:(weather_c[day]*9/5)+32 for day in weather_c }

#print(weather_c)
#print(weather_f)

#EXCERSISE 3
