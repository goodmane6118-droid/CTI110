# Elijah Goodman
# 10/06/25
# Adjust a prior program

print("This program will calculate your travel expenses")

budget = float(input("Please enter your budget: "))
print()
local = input("Please enter your travel destination: ")
print()
gas_cost = float(input("How much will you spend on gas? "))
print()
accom = float(input("How much will you spend on accommodations? "))
print()
food = float(input("Finally, how much will you spend on food? "))
print()

balance = budget - (gas_cost + accom + food)


print("----- Travel Expenses -----")
print(f"{'Location:':20} {local}")
print(f"{'Initial Budget:':20} ${budget:,.2f}")
print(f"{'Gas Cost:':20} ${gas_cost:,.2f}")
print(f"{'Accommodations:':20} ${accom:,.2f}")
print(f"{'Food Cost:':20} ${food:,.2f}")
print("-" * 35)
print(f"{'Remaining Balance:':20} ${balance:,.2f}")