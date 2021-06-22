from coffee_machine.menus import MENU, resources

machine_on = True
profit = 0

def check_resource_availability(choice):
    for item in resources:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry {choice} is not available at the moment")
            return False
    for item in resources:
        resources[item] -= MENU[choice]["ingredients"][item]
    return True

def make_payment(choice):
    global profit
    amount_made = float(input(f"Please Deposit {MENU[choice]['cost']}"))
    amount_made = round(amount_made, 2)
    if amount_made >= MENU[choice]['cost']:
        print(f"You have deposited Rs {amount_made} and Rs {amount_made - MENU[choice]['cost']} has been refunded")
        print(f"Enjoy your {choice}")
        profit += MENU[choice]['cost']

        return True
    else:
        print(f"You have deposited Rs {amount_made} less than {MENU[choice]['cost']}. The amount has been refunded")
        return False



while machine_on:
    choice =  input("What would you like? (tea/coffee/cappuccino):").upper()
    if choice == "OFF":
        machine_on = False
    elif choice == "REPORT":
        print(resources)
        print(f"Money : {profit}")
    elif choice == "TEA" or choice == "COFFEE" or choice == "CAPPUCCINO":
        result = check_resource_availability(choice)
        if result == True:
            make_payment(choice)
    else:
        print("Sorry, we do not have your request in our menu")