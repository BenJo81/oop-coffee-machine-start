from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = 0
coffee_order = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while coffee_order:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        coffee_order = False
    elif user_input == "report":
        print(coffee_maker.report())
    else:
        if coffee_maker.is_resource_sufficient(MenuItem("name")):


