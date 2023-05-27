'''
day 8
'''
#paint area calculator-----------------------------------------------------------------------------

##Write your code below this line 👇
#import math

#def paint_calc(height, width, cover):
#    number_of_cans = math.ceil(height * width / cover)

#    print(f"You will need {number_of_cans} cans of paint")

##Write your code above this line 👆
## Define a function called paint_calc() so that the code below works.   

## 🚨 Don't change the code below 👇
#test_h = int(input("Height of wall: "))
#test_w = int(input("Width of wall: "))
#coverage = 5
#paint_calc(height=test_h, width=test_w, cover=coverage)

#Prime number checker-------------------------------------------------------------------------------

##Write your code below this line 👇

#def prime_checker(number):
#    checker = False
#    for i in range (2, 10):
#        if (number!=i and number%i==0):
#            checker = True

#    if checker==False:
#        print("It's a prime number")
#    else:
#        print("It's not a prime number")
##Write your code above this line 👆
    
##Do NOT change any of the code below👇
#n = int(input("Check this number: "))
#prime_checker(number=n)

#final project - Caesar Cipher-------------------------------------------------------------------------------------

from letters import alphabet
from search import binary_search

def encrypt(input_text, shift):
    output_text = ""
    index_for_shift = 0  #we need to find the index and then shift x numbers
    for i in range (len(input_text)):
        #if the letter in the input text is a space or a symbol then we don't change it just pass it as it is
        if input_text[i] not in alphabet:
            output_text +=  input_text[i]
        #if not that means that is a letter then we shift that letter
        else:
            #finding the place where the letter is
            index_for_shift = binary_search(alphabet, input_text[i], 0, len(alphabet)-1)
            #shifting places for that letter
            index_for_shift += shift
            #adding the shifted letter to the output text
            output_text += alphabet[index_for_shift]

    return output_text

def decrypt(input_text, shift):
    output_text = ""
    index_for_shift = 0  #we need to find the index and then shift x numbers
    for i in range (len(input_text)):
        #if the letter in the input text is a space or a symbol then we don't change it just pass it as it is
        if input_text[i] not in alphabet:
            output_text +=  input_text[i]
        #if not that means that is a letter then we shift that letter
        else:
            #finding the place where the letter is
            index_for_shift = binary_search(alphabet, input_text[i], 0, len(alphabet)-1)
            #shifting places for that letter
            index_for_shift -= shift
            #adding the shifted letter to the output text
            output_text += alphabet[index_for_shift]

    return output_text

loop = "si"

while loop == "si":
    direction = input("\nEscribe 'encode' para encriptar, escribe 'decode' para desencriptar:\n")
    text = input("Escribe tu mensaje:\n").lower()
    shift = int(input("Nivel de encriptamiento: "))
    
    if(direction=="encode"):
        result = encrypt(text, shift)
    elif(direction=="decode"):
        result = decrypt(text, shift)
        
    print(result)
    
    loop = input("¿Desea seguir usando el programa? escriba si o no.")
