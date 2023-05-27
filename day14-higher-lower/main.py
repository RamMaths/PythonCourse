import random
from art import logo, vs
from game_data import data
from screenClear import clear

#Give two cases 
def give_a_case():
    case_one = random.randint(0,len(data))
    case_two = random.randint(0,len(data))
    while case_two==case_one:
        case_two = random.randint(0,len(data))
    return(case_one, case_two)

def show_cases(case1, case2):
    #printing the first thing
    print(data[case1]['name'])
    print(data[case1]['description'])

    #printing the vs art
    print(vs, end="\n\n\n")

    #printing the second thing
    print(data[case2]['name'])
    print(data[case2]['description'])

#defining if the answer was correct or no
def higher_or_lower(guess, case1, case2):
    if guess=="up" and data[case1]['follower_count']>data[case2]['follower_count']:
        return True
    elif guess=="up" and data[case1]['follower_count']<data[case2]['follower_count']:
        return False
    elif guess=="down" and data[case2]['follower_count']>data[case1]['follower_count']:
        return True
    else:
        return False

    
#starting the game--------------------------------------------------

counter=-1
still_playing = True
while still_playing==True:
    clear()
    print(logo, end="\n\n\n------------------------------------------------\n\n-")
    #Giving the two cases
    (case1, case2) = give_a_case()
    
    #showing the cases
    show_cases(case1, case2)
    
    #Ask the user to make the guess
    guess = input("\n\n¿Quien tiene mas seguidores? escribe 'up' o 'down'")
    while guess!="up" and guess!="down":
        guess = input("Escribe 'up' o 'down'")
        
    counter+=1
    still_playing = higher_or_lower(guess, case1, case2)

print(f"Tu puntuacion final es {counter}")
