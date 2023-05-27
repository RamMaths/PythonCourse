MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#requirment 1: print report
def print_report():
    for resource in resources:
        print(f"{resource}= {resources[resource]}")


#the user inserts the coins and we calculate how much was inserted
def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    #how_much is the total amount of money
    how_much = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01) 
    return how_much

def check_resources(option):
    if option=="espresso":
        if resources["water"]>MENU[option]["ingredients"]["water"] and resources["coffee"]>MENU[option]["ingredients"]["coffee"]:
            return True
        else:
            return False
        
    else:
        if resources["water"]>=MENU[option]["ingredients"]["water"] and resources["coffee"]>=MENU[option]["ingredients"]["coffee"] and resources["milk"]>=MENU[option]["ingredients"]["milk"]:
            return True
        else:
            return False


def check_money(option, money):
    if MENU[option]["cost"]>money:
        return money
    elif MENU[option]["cost"]<money:
        return money-MENU[option]["cost"]
    else:
        return money-MENU[option]["cost"]

def options(option, money, machine_resources):
    global profit
    
    if option=="espresso":
        machine_resources["water"] -= MENU[option]["ingredients"]["water"]
        machine_resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
        profit += MENU[option]["cost"]
        return
    else:
        machine_resources["water"] -= MENU[option]["ingredients"]["water"]
        machine_resources["milk"] -= MENU[option]["ingredients"]["milk"]
        machine_resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
        profit += MENU[option]["cost"]
        return



#here starts the system
still_using = "yes"

while still_using=="yes":
    #asking the user for their drink
    option = "report"
    while option!="espresso" and option!="latte" and option!="cappuccino":
        option = input("¿What would you like? (espresso/latte/cappuccino)")
        #if the user ask for a report then we print it 
        if option=="report":
            print_report()
    #asking for the money
    users_money = money()
    #if the machins has the resources required then continue
    if check_resources(option)==True:
        #checking if the user has the money requeired
        change = check_money(option, users_money)
    
        
        if users_money!=change and option!="report":
            options(option, users_money, resources)
            print(f"Here is your change ${change}")
            print(f"Here is your {option}")
        else:
            print("You don't have enough money.")
            exit()
    else:
        print("The machine doesn't have resources")

    still_using = input("Do you want another coffee? type 'yes' or 'no'")

print(f"Today's profit: {profit}")
