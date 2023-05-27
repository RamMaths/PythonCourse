from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu

menu_offer = Menu()
machine = CoffeeMaker()
payment = MoneyMachine()

still_using = "yes"
while still_using=="yes":
    #initializing the while when choosing the drink
    order = "whatever"
    #choosing the drink only if the user types one of the correct options
    while order!="latte" and order!="espresso" and order!="cappuccino":
        order = input(f"What do you want to order? {menu_offer.get_items()}")
        #if the user types report we print a rport of all resources
        if order=="report":
            machine.report()
        if order=="profit":
            payment.report()

        if order=="latte" or order=="espresso" or order=="cappuccino":
            #finding the drink whithin the menu
            drink = menu_offer.find_drink(order)

            if machine.is_resource_sufficient(drink)==True:
                if payment.make_payment(drink.cost)==True:
                    machine.make_coffee(drink)

    still_using = input("Do you want another coffee? type 'yes' or 'no'")
