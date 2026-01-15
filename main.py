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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COIN_VALUE = {
    "Quarters": .25,
    "Dimes": .10,
    "Nickles": .05,
    "Pennies": .01,

}

Profit = 0

# Type

# TODO: 1. Print report of all the coffee machine resources
def coffee_machine_resources():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f"Water = {water}ml\nMilk = {milk}ml\nCoffee = {coffee}g\nProfit = ${Profit}")

# TODO: 2. Prompt user to pay with change
def transaction(drink):
    Paid = False
    global Profit
    while not Paid:
        print("Please insert coins")
        Q_Payment = int(input("How many Quarters?: "))
        Q_Payment *= COIN_VALUE['Quarters']
        D_Payment = int(input("How many Dimes?: "))
        D_Payment *= COIN_VALUE['Dimes']
        N_Payment = int(input("How many Nickles?: "))
        N_Payment *= COIN_VALUE['Nickles']
        P_Payment = int(input("How many Pennies?: "))
        P_Payment *= COIN_VALUE['Pennies']
        total_payment = Q_Payment + D_Payment + N_Payment + P_Payment
        if MENU[drink]['cost'] < total_payment:
            change = round(total_payment - MENU[drink]['cost'],2)
            print(f"Your change is {change}, enjoy your {drink}")
            Profit += MENU[drink]['cost']
            Paid = True
        elif MENU[drink]['cost'] > total_payment:
            print(f"That is not enough for a {drink}, here's your refund")
            Paid = True

# TODO: 3. Figure out how to add money made together
# TODO: 4. When ingredients run out say we can't make that specific item.


off = False
while not off:
    users_drink = input("What would you like? (espresso/latte/cappuccino)? ").strip().lower()
    if users_drink == 'espresso':
        if resources['water'] < 50 or resources['coffee'] < 18:
            print(f"We can't make {users_drink}, we are out of the ingredients for it.")
        else:
            print(f"That will cost {MENU['espresso']['cost']}.")
            transaction(users_drink)
            resources["water"] -= MENU['espresso']['ingredients']['water']
            resources["coffee"] -= MENU['espresso']['ingredients']['coffee']
    elif users_drink == 'cappuccino':
        if resources['water'] < 250 or resources['coffee'] < 24 or resources['milk'] < 100:
            print(f"We can't make {users_drink}, we are out of the ingredients for it")
        else:
            print(f"That will cost {MENU['cappuccino']['cost']}.")
            transaction(users_drink)
            resources["water"] -= MENU['cappuccino']['ingredients']['water']
            resources["coffee"] -= MENU['cappuccino']['ingredients']['coffee']
            resources["milk"] -= MENU['cappuccino']['ingredients']['milk']
    elif users_drink == 'latte':
        if resources['water'] < 200 or resources['coffee'] < 24 or resources['milk'] < 150:
            print(f"We can't make {users_drink}, we are out of the ingredients for it.")
        else:
            print(f"That will cost {MENU['latte']['cost']}.")
            transaction(users_drink)
            resources["water"] -= MENU['latte']['ingredients']['water']
            resources["coffee"] -= MENU['latte']['ingredients']['coffee']
            resources["milk"] -= MENU['latte']['ingredients']['milk']
    elif users_drink == 'report':
        coffee_machine_resources()
    else:
        off = True









