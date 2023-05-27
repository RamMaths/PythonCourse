import random
from screenClear import clear

logo = '''
 ██████╗█████╗███╗   ██╗    ██╗   ██╗██████╗██╗   ██╗     ██████╗██╗   ███████████████████████╗    ██████╗ 
██╔════██╔══██████╗  ██║    ╚██╗ ██╔██╔═══████║   ██║    ██╔════╝██║   ████╔════██╔════██╔════╝    ╚════██╗
██║    █████████╔██╗ ██║     ╚████╔╝██║   ████║   ██║    ██║  █████║   ███████╗ ██████████████╗      ▄███╔╝
██║    ██╔══████║╚██╗██║      ╚██╔╝ ██║   ████║   ██║    ██║   ████║   ████╔══╝ ╚════██╚════██║      ▀▀══╝ 
╚████████║  ████║ ╚████║       ██║  ╚██████╔╚██████╔╝    ╚██████╔╚██████╔█████████████████████║      ██╗   
 ╚═════╚═╝  ╚═╚═╝  ╚═══╝       ╚═╝   ╚═════╝ ╚═════╝      ╚═════╝ ╚═════╝╚══════╚══════╚══════╝      ╚═╝   

'''
still_playing = "si"
while still_playing=="si":
    CORRECT_ANSWER = random.randint(1,101)
    lose = True

    clear()
    print(logo)
    print("Estoy pensando en un numero del 1 al 100")
    difficult = input("Elige la dificultad. Escribe 'easy' para un nivel facil y 'hard' para uno dificl.")
    while difficult!="easy" and difficult!="hard":
        difficult = input("Elige una opcion de las de arriba.")
    if difficult=="easy":
        attempts_number = 10
    else:
        attempts_number = 5
    
    while attempts_number>0:
        guess = int(input(f"Intento {attempts_number}: "))
        if guess>CORRECT_ANSWER:
            print("La respuesta es menor")
            attempts_number-=1
        elif guess<CORRECT_ANSWER:
            print("La respuesta es mayor")
            attempts_number-=1
        else:
            lose = False
            break

    if lose==True:
        print("Ya no te quedan intentos, perdiste...")
    else:
        print("Acertaste!!!")


    still_playing = input("¿Deseas jugar de nuevo? escribe si o no: ")
    while still_playing!="si" and still_playing!="no":
        still_playing = input("Escriba si o no: ")
