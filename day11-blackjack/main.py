import random
from screenClear import clear
from art import cards_design, logo

#cards and its values
cards_value = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

#assigning a card
def assign_card():
    return random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

def showing_cards(cards):
    for card in (cards):
        print(cards_design[card], end="\n")


def calculate_player_points(cards):
    ace_value = 0
    total_points = 0
    for card in cards:
        if card == "A":
            ace_value = int(input("¿Que valor le quieres dar al as? 1 u 11:"))
            while ace_value!=1 and ace_value!=11:
                ace_value = int(input("Elige un valor valido 1 u 11: "))
            total_points += ace_value
        else: 
            total_points += cards_value[card]

    return total_points

def calculate_computer_points(cards):
    ace_value = 0
    total_points = 0
    for card in cards:
        if card == "A":
            ace_value = random.choice([1,11])
            total_points += ace_value
        else: 
            total_points += cards_value[card]

    return total_points

#starting the game--------------------------------------

#variables
add_cards = "si"
play_again = "si"
player_cards = []
computer_cards = []
player_points = 0
computer_points = 0

while play_again=="si":
    player_cards.clear()
    computer_cards.clear()
    player_points = 0
    computer_points = 0

    clear()
    print(logo)
    input("\nPresiona enter para continuar...")
    #assigning a card to the player
    player_cards.append(assign_card())
    #assigning a card to the computer
    computer_cards.append(assign_card())
    computer_cards.append(assign_card())

    #showing the cards
    print("\n\nTu tienes estas cartas ", end="")
    showing_cards(player_cards)
    add_cards = input("¿Deseas añadir otra? escribe si o no: ")
    while add_cards=="si":
        player_cards.append(assign_card())
        clear()
        print(logo)
        print("Tu tienes estas cartas ", end="")
        showing_cards(player_cards)
        add_cards = input("¿Deseas añadir otra? escribe si o no: ")

    #evaluating the points
    player_points = calculate_player_points(player_cards)
    computer_points = calculate_computer_points(computer_cards)

    #showing computer cards
    print("\nLa computadora tiene estas cartas ")
    showing_cards(computer_cards)

    #evaluating the game 
    if player_points>computer_points and player_points<=21:
        print("\nGanaste!!")
    elif computer_points>player_points and computer_points<=21:
        print("\nLa computadora gana.")
    elif computer_points>player_points and computer_points>21 and player_points<=21:
        print("\nGanaste!!")
    elif player_points>computer_points and player_points>21 and computer_points<=21:
        print("\nLa computadora gana.")
    else:
        print("\nEs un empate.")

    play_again = input("¿Quieres jugar de nuevo? Escribe si o no: ")
