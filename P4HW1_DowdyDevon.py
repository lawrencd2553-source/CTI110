# Devon Dowdy
# 07/05/2026
# P4HW1
# stores grade

#Start
 # DISPLAY "Enter the number of scores you want to input: "
#READ num_scores

#READ scores_list as an empty list

#FOR i FROM 1 TO num_scores DO
#   INITIALIZE is_valid to False

 #   WHile is_valid is False DO
 #       DISPLAY "Enter score ", i, ": "
 #       READ score

#        IF score >= 0 AND score <= 100 THEN
 #           APPEND score to scores_list
  #          SET is_valid to True
   #     ELSE
    #        DISPLAY "INVALID SCORE ENTERED!!!!!"
     #       DISPLAY "Please enter a score between 0 and 100."
      #      DISPLAY "Please try again."
       #     ENDIF
        # ENDWHILE
#ENDFOR
#IF scores_list is not empty THEN
#SET lowest_score = MINIMUM(scores_List)
#DISPLAY "Lowest score enteredL " + lowest_score"
#INIIALIZE modified_list as copy of scores_list
#REMOVE lowest_score from modified_list
#DISPLAY "scores_list with lowest score removed: " + modified_list
#IF modified_list is not empty THEN
#   SET average = SUM(modified_list) / LENGTH(modified_list)
#Else
#   SET average = lowest_score
#ENDIF
#DISPLAY "Average score: " + average
#IF average >= 90 THEN
#   DISPLAY "letter_grade: A"
#ELSE IF average >= 80 THEN
#   DISPLAY "letter_grade: B"
#ELSE IF average >= 70 THEN
#   DISPLAY "letter_grade: C"
#ELSE IF average >= 60 THEN
#   DISPLAY "letter_grade: D"
#ELSE
#   DISPLAY "letter_grade: F"
#ENDIF
#DISPLAY "letter_grade: " + letter_grade
#ENDIF
#Display " Letter Grade: " + letter_grade
#ENDIF
#END
num_scores = int(input("Enter the number of scores you want to input: "))

scores_list = []

for i in range(1, num_scores +1):
    while True:
        score = float(input(f"Enter score {i}: "))
        if 0 <= score <= 100:
            scores_list.append(score)
            break
        else:
           print("INVALID SCORE ENTERED!!!!!")
           print("Please enter a score between 0 and 100.")
           print("Please try again.")

print("\n" + "-"*12 + "Results" + "-"*12)

lowest_score = min(scores_list)
print(f"Lowest Score: {lowest_score:<20}")

modified_list = scores_list.copy()
modified_list.remove(lowest_score)
print(f"Modified List: {modified_list}")

average = sum(modified_list) / len(modified_list) if modified_list else lowest_score
print(f"Average Score: {average:<20.2f}")

if average >= 90:
    print("letter_grade: A")   
elif average >= 80:
    print("letter_grade: B")
elif average >= 70:
    print("letter_grade: C")
elif average >= 60:
    print("letter_grade: D")
else:
    print("letter_grade: F")

print(f"{letter_grade:':<20}{letter_grade}")
print("-"*30)