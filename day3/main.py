"""
day 3
"""

## 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
## 🚨 Don't change the code above 👆

##Write your code below this line 👇

#remainder = number % 2
 
#if remainder == 0:
#    print("This is an even number.")
#else:
#    print("This is an odd number.")  

#------------------------------------------------------------------------------------------------------------------------------------

### 🚨 Don't change the code below 👇
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
### 🚨 Don't change the code above 👆

###Write your code below this line 👇
#rounded_BMI = round(weight / height ** 2)
#if(rounded_BMI < 18.5):
#    print(f"Your BMI is {rounded_BMI}, you are underweight.")
#elif(rounded_BMI >= 18.5 and rounded_BMI < 25):
#    print(f"Your BMI is {rounded_BMI}, you have a normal weight.")
#elif(rounded_BMI >= 25 and rounded_BMI < 30):
#    print(f"Your BMI is {rounded_BMI}, you are slightly overweight.")
#elif(rounded_BMI >= 30 and rounded_BMI < 35):
#    print(f"Your BMI is {rounded_BMI}, you are obese.")
#else:
#    print(f"Your BMI is {rounded_BMI}, you are clinically obese.")
    
#------------------------------------------------------------------------------------------------------------------------------------

## 🚨 Don't change the code below 👇
#year = int(input("Which year do you want to check? "))
## 🚨 Don't change the code above 👆

##Write your code below this line 👇

#if((year%4)==0):
#    if(year%100)==0:
#        if((year%400)==0):
#            print("Leap year.")
#        else:
#            print("Not leap year.")
#    else:
#        print("Leap year.")
#else:
#    print("Not leap year.")

#------------------------------------------------------------------------------------------------------------------------------------

## 🚨 Don't change the code below 👇
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
## 🚨 Don't change the code above 👆

##Write your code below this line 👇
#if(size == "S"):
#    total_bill = 15
#    if(add_pepperoni == "Y"):
#        total_bill += 2
#elif(size == "M"):
#    total_bill = 20
#    if(add_pepperoni == "Y"):
#        total_bill += 3
#elif(size == "L"):
#    total_bill = 25
#    if(add_pepperoni == "Y"):
#        total_bill += 3

#if(extra_cheese == "Y"):
#    total_bill += 1
 
#print(f"Your final bill is: ${total_bill}.")

#-------------------------------------------------------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_sum = 0
love_sum = 0

name1.lower()
name2.lower()

#for you
true_sum += name1.count('t')
true_sum += name1.count('r')
true_sum += name1.count('u')
true_sum += name1.count('e')
love_sum += name1.count('l')
love_sum += name1.count('o')
love_sum += name1.count('v')
love_sum += name1.count('e')
print(true_sum)
print(love_sum)

#for your mate
true_sum += name2.count('t')
true_sum += name2.count('r')
true_sum += name2.count('u')
true_sum += name2.count('e')
love_sum += name2.count('l')
love_sum += name2.count('o')
love_sum += name2.count('v')
love_sum += name2.count('e')
print(true_sum)
print(love_sum)

#lOVE SOCRE
love_score = str(true_sum) + str(love_sum)
love_score = int(love_score)

if(love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score>=40 and love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
