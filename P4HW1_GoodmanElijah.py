#  Elijah Goodman 
#  11/1/25
#  P4HW1
#  Create a program that organizes user input into a list of scores.



num_scores = int(input("How many scores would you like to enter? "))


score_list = []

for i in range(num_scores):
    valid = False
    while not valid:  
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            score_list.append(score)
            valid = True
        else:
            print("Invalid score! Please enter a value between 0 and 100.")


lowest_score = min(score_list)


modified_list = score_list.copy()
modified_list.remove(lowest_score)


average_score = sum(modified_list) / len(modified_list)


if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"


print("\n--------- Results -----------")
print("Lowest Score:", lowest_score)
print("Modified List:", modified_list)
print(f"Scores Average: {average_score:.2f}")
print("Grade:", grade)
print("-------------------------------")


#Pseudocode:

# START
#   Display "How many scores would you like to enter?"
#   Input num_scores
#   Create an empty list called score_list
#   FOR count from 1 to num_scores DO
#       Set valid = False
#      WHILE valid = False DO
#           Display "Enter score #" + count
#           Input score
#          IF score < 0 OR score > 100 THEN
#              Display "Invalid score! Please enter a value between 0 and 100."
#          ELSE
#             Append score to score_list
#              Set valid = True
#       END WHILE
#   END FOR
#   Find the lowest score from score_list → lowest_score
#   Create a new list called modified_list that is a copy of score_list
#   Remove lowest_score from modified_list
#   Calculate average = sum(modified_list) / length(modified_list)
#   IF average >= 90 THEN grade = 'A'
#   ELSE IF average >= 80 THEN grade = 'B'
#   ELSE IF average >= 70 THEN grade = 'C'
#   ELSE IF average >= 60 THEN grade = 'D'
#   ELSE grade = 'F'
#   Display "Lowest score entered:", lowest_score
#   Display "Score list after dropping lowest:", modified_list
#   Display "Average of modified list:", average
#   Display "Letter grade:", grade
# END