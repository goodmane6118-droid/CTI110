#Elijah Goodman 
#10/20/25
#P3HW2
#Create a program which prompts a user their name, hours of work, pay rate, overtime hours, and calculate the amount that user should be paid.





employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's hourly pay rate: "))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
else:
    overtime_hours = 0

regular_hours = min(hours_worked, 40)
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (1.5 * pay_rate)
gross_pay = regular_pay + overtime_pay

print("-------------------------------------------------------------------------------------")
print(f"Employee Name:        {employee_name}\n")
print("Hours Worked  Pay Rate  OverTime   OverTime Pay  RegHour Pay  Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}"
      f"{overtime_pay:<13.2f}${regular_pay:<13.2f}${gross_pay:<.2f}")

#Start
  #prompt user for their name
  #prompt user for their number of hours worked
  #prompt user for theri pay rate
  #if hours worked > 40
     #overtime hours = hours worked - 40
   #else 
      #overtime hours = 0
  #regular_hours = min(hours_worked, 40)
  #regular_pay = regular_hours * pay_rate
  #overtime_pay = overtime_hours * (1.5 * pay_rate)
  #gross_pay = regular_pay + overtime_pay

  #display user results
#Stop