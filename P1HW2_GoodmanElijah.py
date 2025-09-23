# Elijah Goodman 
# 09/23/25
# P1HW2
# Create a program that does basic math on numbers entered by user.


print(" This program will caluclate your travel expenses")

budget = int(input("Please enter your budget:"))
print()
local = input("Please enter your travel destination:")
print()
gas_cost = int(input("How much will you spend on gas?"))
print()
accom = int(input("How much will you spend on accomodations?"))
print()
food = int(input("Finally, how much will you spend on food?"))
balance = budget - (gas_cost + accom + food)
print()


print("-----Travel Expenses-----")
print("\n")
print("Your budget:", budget)
print("Loaction:", local)
print("\n")
print("Gas Cost:", gas_cost)
print("Accomodations:", accom)
print("Food Cost:", food)
print("\n")
print("Your Remaining Balance:", balance)

#START
  #prompt user for budget number 
  #prompt user for travel location 
  #prompt user for expenses on gas 
  #prompt user for expenses on accomodations
  #prompt user for expenses on food 
  #balance = budget - (gas price + accomodations + food)
  #Dislay balance 
#END
