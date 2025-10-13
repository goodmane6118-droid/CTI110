#Elijah Goodman 
#10/07/25
#P3LAB
#Allow user to enter money values and calculate an efficent number of coins and paper money needed to make a given amount of money.


amount = float(input("Enter the amount of money as a float: $"))
cents = int(round(amount * 100))
dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents

if cents == 0:
    print("No change")

if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(f"{pennies} Pennies")