#Elijah Goodman
#12/01/25
#P5LAB
#Create a program that emulates a self-checkout machine.

import random

def disperse_change(change):
    cents = int(round(change * 100))
    dollars = cents // 100
    cents = cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    pennies = cents

    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    amount_paid = float(input("How much will you put in the self-checkout? $"))

    change = amount_paid - amount_owed
    if change < 0:
        print(f"Not enough money. You still owe ${-change:.2f}.")
    else:
        print(f"Change is: ${change:.2f}")
        disperse_change(change)


if __name__ == "__main__":
    main()
