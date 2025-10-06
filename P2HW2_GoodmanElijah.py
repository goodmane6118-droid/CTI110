# ELijah Goodman 
# 10/06/25
#P2HW2
# Design a program that prompt users for their grades for module tests and put the entered scores in an organzied list

print("Enter your grades for each module below.")

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

module_grades = [module1, module2, module3, module4, module5, module6]


lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print("------------ Results ------------")
print(f"{'Lowest Grade:':20} {lowest}")
print(f"{'Highest Grade:':20} {highest}")
print(f"{'Sum of Grades:':20} {total}")
print(f"{'Average:':20} {average:.2f}")
print("---------------------------------------")

#START
# Prompt user to enter grade scores for each module:
#   Module 1
#   Module 2
#   Module 3
#   Module 4
#   Module 5
#   Module 6
# Create list called 'module_grades'.
# Calculate the grade scores
#    The lowest grade using min()
#    The highest grade using max()
#    The total (sum) using sum()
#    The average (total / number of grades)
# Display the results clearly with labels and alignment.
# Average should display with two decimal places.
#STOP