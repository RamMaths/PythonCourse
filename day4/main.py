import random

##Remember to use the random module
##Hint: Remember to import the random module here at the top of the file. 🎲
	 
## 🚨 Don't change the code below 👇
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)
# # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
##Write the rest of your code below this line 👇

#random_decision = random.randint(0,1)

#if(random_decision==1):
#    print("Heads")
#else:
#    print("Tails")

#------------------------------------------------------------------------------------------------

## Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
## 🚨 Don't change the code above 👆

##Write your code below this line 👇

#selected_name = random.randint(0, (len(names)-1))
#print(f"{names[selected_name]}, is going to buy the meal today!")

#------------------------------------------------------------------------------------------------

## 🚨 Don't change the code below 👇
#row1 = ["⬜️","⬜️","⬜️"]
#row2 = ["⬜️","⬜️","⬜️"]
#row3 = ["⬜️","⬜️","⬜️"]
#map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
#position = input("Where do you want to put the treasure? ")
## 🚨 Don't change the code above 👆

##Write your code below this row 👇

##coordenade x
#x =  int(position[1]) - 1
#y =  int(position[0]) - 1
#map[x][y] = "X"
##Write your code above this row 👆

## 🚨 Don't change the code below 👇
#print(f"{row1}\n{row2}\n{row3}")

#-----------------------------------------------------------------------------------------------
# PAPER AND SCISSORS PROJECT
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_election = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))
computer_election = random.randint(0,2)

if(player_election == 0):
    print("\nyou choose:")
    print(rock)
    if(computer_election==0):
        print("\ncomputer choose:")
        print(rock)
        print("\nTIE no one wins")
    elif(computer_election==1):
        print("\ncomputer choose:")
        print(paper)
        print("\nYou lose, copmuter won")
    else:
        print("\ncomputer choose:")
        print(scissors)
        print("\nYou win")
elif(player_election == 1):
    print("\nyou choose:")
    print(paper)
    if(computer_election==0):
        print("\ncomputer choose:")
        print(rock)
        print("\nYou win")
    elif(computer_election==1):
        print("\ncomputer choose:")
        print(paper)
        print("\nTIE no one wins")
    else:
        print("\ncomputer choose:")
        print(scissors)
        print("\nYou lose, copmuter won")
else:
    print("\nyou choose:")
    print(scissors)
    if(computer_election==0):
        print("\ncomputer choose:")
        print(rock)
        print("\nYou lose, copmuter won")
    elif(computer_election==1):
        print("\ncomputer choose:")
        print(paper)
        print("\nYou win")
    else:
        print("\ncomputer choose:")
        print(scissors)
        print("\nTIE no one wins")
