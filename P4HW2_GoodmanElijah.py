#  Elijah Goodman 
#  11/1/25
#  P4HW2
#  Create a program that calculates the salary for multiple employees.







total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

print("Enter employee information. Type 'Done' when finished.\n")

employee_name = input("Enter employee's name: ")


while employee_name != "Done":
    hours_worked = float(input(f"Enter number of hours worked for {employee_name}: "))
    pay_rate = float(input(f"Enter hourly pay rate for {employee_name}: "))

    
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
    else:
        overtime_hours = 0

    regular_hours = min(hours_worked, 40)
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (1.5 * pay_rate)
    gross_pay = regular_pay + overtime_pay

    
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    

    
    print("\nHours Worked  Pay Rate  OverTime   OverTime Pay  RegHour Pay  Gross Pay")
    print("-------------------------------------------------------------------------------------")

    print(f"{hours_worked:<14.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}"
          f"{overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<.2f}")

    
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ")



print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid for gross: ${total_gross_pay:.2f}")

#  Pseudocode:

#  START
#   Initialize total_regular_pay = 0
#   Initialize total_overtime_pay = 0
#   Initialize total_gross_pay = 0
#   Initialize employee_count = 0
#   Display instructions to user
#   Input employee_name
#   WHILE employee_name != "Done" DO
#       Input hours_worked
#      Input pay_rate
#      IF hours_worked > 40 THEN
#          overtime_hours = hours_worked - 40
#          regular_hours = 40
#      ELSE
#          overtime_hours = 0
#          regular_hours = hours_worked
#      ENDIF
#      Calculate regular_pay = regular_hours * pay_rate
#      Calculate overtime_pay = overtime_hours * (1.5 * pay_rate)
#      Calculate gross_pay = regular_pay + overtime_pay
#      Display the employee’s pay information formatted in table style
#      Add regular_pay to total_regular_pay
#      Add overtime_pay to total_overtime_pay
#      Add gross_pay to total_gross_pay
#      Add 1 to employee_count
#      Ask user for next employee name
#   END WHILE
#   Display total number of employees, total regular pay, total overtime pay, total gross pay
# END

