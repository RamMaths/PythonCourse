'''
day 10
'''

#days in a month--------------------------------------------------------------------

#def is_leap(year):
#  if year % 4 == 0:
#    if year % 100 == 0:
#      if year % 400 == 0:
#        return True
#      else:
#       return False
#    else:
#        return True
#  else:
#       return False

#def days_in_month(year, month):
#  month_days = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#  month -= 1
#  if(month==1):
#      if(is_leap(year)==True):
#          return 29
#      else:
#          return 28
  
#  return month_days[month]
  
  
##🚨 Do NOT change any of the code below 
#year = int(input("Enter a year: "))
#month = int(input("Enter a month: "))
#days = days_in_month(year, month)
#print(days)

# Calculator-------------------------

from art import logo
from screenClear import clear

#Add
def add(n1, n2):
    """
    adds a number to another and returns the result
    """
    return n1 + n2
#Substract
def substract(n1, n2):
    """
    substracts a number to another and returns the result
    """
    return n1 - n2
#Multiply
def multiply(n1, n2):
    """
    multiplies a number to another and returns the result
    """
    return n1 * n2
#Divide
def divide(n1, n2):
    """
    divides a number to another and returns the result
    """
    return n1 / n2

#declaring variables
still_using = "si"

#operations

operations ={
    "+": "add",
    "-": "substract",
    "*": "multiply",
    "/": "divide"
}

print(logo)

num1 = int(input("\n\nIngresa el primer numero: "))
#printing and choosing the operations avilable
for operation in operations:
    print(operation)
    
operation_symbol = input("Ingresa una operacion de las opciones de arriba: ")
    
num2 = int(input("Ingresa el segundo numero: "))
    
#making the calculation
calculation_function = operations[operation_symbol]
answer = eval(calculation_function +  "(num1,num2)")
print(answer)

#answering if they want to loop the program
still_using = input("¿Quieres usar el resultado para otra operacion? ingresa si o no: ")


#looping until the user says no
while still_using == "si":
    clear()
    print(logo)
    print(f"Estas usando el numero: {answer}")
    #printing the operations avilable
    for operation in operations:
        print(operation)
    
    operation_symbol = input("Ingresa una operacion de las opciones de arriba: ")
    
    num2 = int(input("Ingresa el segundo numero: "))
    
    calculation_function = operations[operation_symbol]
    answer = eval(calculation_function +  "(answer,num2)")
    print(answer)

    still_using = input("¿Quieres usar el resultado para otra operacion? ingresa si o no: ")
