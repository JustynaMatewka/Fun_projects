from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#   Najpierw trzeba utworzyć nowy obiekt dla każdej z klas, żeby powstała nasz prywatna kopia elementu
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
turn_on = True


while turn_on:
    user_choice = input(f"What would you like? ({menu.get_items()}):").lower()

    if user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        user_choice_object = menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(user_choice_object):
            if money_machine.make_payment(user_choice_object.cost):
                coffe_maker.make_coffee(user_choice_object)
    elif user_choice == "off":
        turn_on = False
        print("Coffee machine is going to sleep.")
    else:
        print(f"{user_choice.capitalize()} is a wrong input.")
