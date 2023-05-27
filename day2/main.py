
"""
day 2
"""

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# # ###################################

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# print (two_digit_number[0] + " + " + two_digit_number[1] + " = " + str(first_digit + second_digit))
# print (first_digit + second_digit)

#----------------------------------------------------------------------------------------------------------------------------

### 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
### 🚨 Don't change the code above 👆

###Write your code below this line 👇
#float(height)
#float(weight)

#BMI =  int(float(weight) / float(height)**2)
#print(BMI)

#----------------------------------------------------------------------------------------------------------------------------

## 🚨 Don't change the code below 👇
#age = input("What is your current age?")
## 🚨 Don't change the code above 👆

##Write your code below this line 👇
#age = 90 - int(age)

#days = int(age) * 365
#weeks = int(age) * 52
#months = int(age) * 12

#print("You have " + str(days) + " days, " + str(weeks) + " weeks, and " + str(months) + " months left.")

#-----------------------------------------------------------------------------------------------------------------------------

#final project

print("Werlcome to the tip calculator.")
total_bill = float(input("What was the total bil? $"))
percentage = int(input("What percentage would you want to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill += (total_bill * (percentage/100))
each_person = total_bill / people
each_person = round(each_person, 2)

print(f"Each person should pay: ${each_person}")
