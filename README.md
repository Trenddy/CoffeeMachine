☕ Coffee Machine Simulation in Python

This is a simple terminal-based coffee machine simulator written in Python. It allows users to "order" coffee (espresso, latte, or cappuccino), insert coins to pay, and receive change. The machine tracks its available resources and profit throughout its operation.

📌 Features

Three types of drinks: espresso, latte, and cappuccino

Checks for sufficient ingredients before preparing the drink

Accepts virtual coins (quarters, dimes, nickels, and pennies)

Calculates and returns change if overpaid

Tracks and displays current resources (water, milk, coffee)

Displays total profit from sales

report command for checking machine status

Shuts down on any invalid input (or user request)

🧾 How It Works
Startup

Upon running, the machine continuously prompts the user:

What would you like? (espresso/latte/cappuccino)?

Orders

When a valid drink is chosen:

It checks if there are enough resources.

If sufficient, it asks the user to insert coins:

How many Quarters?:
How many Dimes?:
How many Nickles?:
How many Pennies?:


If payment is sufficient, it deducts resources and updates profit.

If payment is insufficient, it refunds the user.

Report

Type report to print a summary of:

Remaining water (ml)

Remaining milk (ml)

Remaining coffee (g)

Total profit ($)

Exit

Entering anything else will stop the machine:

What would you like? (espresso/latte/cappuccino)? <anything else>

🔧 Code Structure
MENU

A dictionary storing available drinks, ingredients, and cost.

resources

Current inventory of ingredients in the machine.

COIN_VALUE

Dictionary mapping coin types to their monetary value.

Key Functions

coffee_machine_resources() – prints a status report

transaction(drink) – handles coin input, payment validation, and updates profit

🛠️ Possible Improvements

Wrap code into functions or classes for better modularity

Add unit tests for functions

Refactor the repetitive drink logic into reusable code

Add support for more drinks or customization (e.g., sugar level)

Allow user to turn off the machine explicitly (e.g., off command)

✅ Requirements

Python 3.x

Run the script:

python coffee_machine.py

🧠 Author Notes

This project is perfect for beginners learning:

Control flow

Functions

Dictionaries

Loops and conditionals

Basic simulation of a real-world machine
