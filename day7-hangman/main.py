'''
day 7 - hangaman project
'''
import random
from hangman_art import stages, logo
from hangman_words import word_list
import screenClear
#game presentation
print(logo)
input("\n\nPresiona enter para continuar...")


# step 1 - picking random words and cheking answers

player_word = random.choice(word_list)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

player_word_length = len(player_word)
display = []
for i in range(player_word_length):
    display.append("_")

#TODO-2: 
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#total of attempts to answer the word
attempts = 6

while attempts>0:
    screenClear.screen_clear()
    print(stages[attempts])
    #printing the display
    for i in range(len(display)):
        print(display[i], end=" ")
    guess = input("\n\nAdivina una letra: ").lower()
    counter = 0
    attempts_check = False
    
    #cheking the letters in the word
    for letter in player_word:
        if guess == letter:
            display[counter] = letter
            attempts_check=True
        counter += 1
    
    #checking if the player didn't guess the letter
    if attempts_check == False:
        attempts -= 1 

    
    #if the player wins
    if "_" not in display:
        print("\nGanaste!!!")
        break

# if the player is out of lives or attempts
if attempts == 0:
    screenClear.screen_clear()
    print(stages[0])
    print(f"Perdiste, la respuesta correcta era {player_word}")


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


