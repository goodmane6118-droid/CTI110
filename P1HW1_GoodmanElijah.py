# Elijah Goodman 
# 09/23/25
# P1HW1
# Create a program with input and print functions. 


print("-----Calculating Exponents----")
print("\n")

base_value = int(input("Enter an interger as the base value:"))
print()
exponent = int(input("Enter an integer as the exponent:"))
print()

result_ex = pow(base_value, exponent)
print (base_value,"raised to the power of", exponent, "is", str(result_ex) + "!!")
print("\n")
print("-----Addition and Subtraction----")
print("\n")
str_int = int(input("Enter a starting interger:"))
print()
add_int = int(input("Enter an integer to add:"))
print()
sub_int = int(input("Enter an integer to subtract:"))
print()

result_add = str_int + add_int - sub_int
print(str_int, "+", add_int, "-", sub_int, "is equal to", result_add)