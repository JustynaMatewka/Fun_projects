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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

def share_report(current_resources):
    print(f"Water: {current_resources['water']}ml\n"
          f"Milk: {current_resources['milk']}ml\n"
          f"Coffee: {current_resources['coffee']}g\n"
          f"Money: ${current_resources['money']}")

def check_resources(current_resources, coffee_type):
    for ingredient in MENU[coffee_type]['ingredients']:
        if not MENU[coffee_type]['ingredients'][ingredient] <= current_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.”")
            return False
    return True

def collect_coins():
    user_coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }

    print("Please insert coins.")
    user_coins['quarters'] = int(input("How many quarters?: "))
    user_coins['dimes'] = int(input("How many dimes?: "))
    user_coins['nickles'] = int(input("How many nickles?: "))
    user_coins['pennies'] = int(input("How many pennies?: "))
    return calculate_coins(user_coins)

def calculate_coins(given_coins):
    return COINS['quarters'] * given_coins['quarters'] + COINS['dimes'] * given_coins['dimes'] + COINS['nickles'] * given_coins['nickles'] + COINS['pennies'] * given_coins['pennies']

def check_transaction_successful(current_resources, given_coins, coffee_type):
    if given_coins < MENU[coffee_type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if given_coins > MENU[coffee_type]['cost']:
        change = given_coins - MENU[coffee_type]['cost']
        print(f"Here is ${change} dollars in change.")

    current_resources['money'] += MENU[coffee_type]['cost']
    return True

def make_coffee(current_resources, coffee_type):
    if check_resources(current_resources, coffee_type):
        if check_transaction_successful(current_resources, collect_coins(), coffee_type):
            for ingredient in MENU[coffee_type]['ingredients']:
                current_resources[ingredient] -= MENU[coffee_type]['ingredients'][ingredient]
            print(f"Here is your {coffee_type}. Enjoy!")
        else:
            return
        return
    else:
        return



turn_on = True
resources = {
    "water": 10000,
    "milk": 5000,
    "coffee": 760,
    "money": 0
}

while turn_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice == "report":
        share_report(resources)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        make_coffee(resources, user_choice)
    elif user_choice == "off":
        turn_on = False
        print("Coffee machine is going to sleep.")
    else:
        print(f"{user_choice.capitalize()} is a wrong input.")