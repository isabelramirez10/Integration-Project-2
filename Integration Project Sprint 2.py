# Isabel Ramirez
# This program will help students manage their time dedicated to
# each class based on current grade, difficulty and study time.
name = input("Enter name: ")
print("Hello", name + ".")
# Using a + instead of a comma prevents there from
# being a space between the user's name and the period.

print("I am your personal study management assistant.", end=' ')
# the website Geeks for Geeks helped me understand the end argument.
# Since there is a space as the end argument, a space will appear at the end
# of the printed statement and combine it with the next line.

credit_hours = int(float(input("How many credit hours are you taking? ")))
min_study_time = credit_hours * 2
max_study_time = credit_hours * 3
# Students should dedicate two to three hours for every credit hour.

number_of_classes = input("How many classes are you taking? ")

print("You should dedicate", min_study_time, "to", max_study_time, "hours per week to studying.")
actual_study_time = int(float(input("How many hours per week do you currently dedicate to studying? ")))
study_time_difference = max_study_time - actual_study_time
# This equation is to display to the user the number of
# hours they could be studying compared to what they are now.

print("You could be studying up to", study_time_difference, "hours more per week.")
print("If you feel as though you need additional time, go to your professors' office hours.")
hardest_class = input("Which is your most difficult class: ")
hardest_credits = int(float(input("How many credit hours is it? ")))
hardest_class_grade = int(float(input("Enter your grade: ")))

if hardest_class_grade < 70:
    print("You should consider going to office hours if you have not done so already.")
else:
    print("Even if you think you do not need it, "
          "consider office hours.")

hardest_class_hours = int(float(input("Enter the number of hours per week you study for this class: ")))
hardest_class_total_time = hardest_class_hours * 2
# This is the minimum number of hours recommended to dedicate to the subject outside of class.

print("You should dedicate at least ", format(hardest_class_total_time, '.2f'),
      " hours outside of class to ", hardest_class + ".", sep="")
hardest_class_office_hours = (hardest_class_hours // 2)
# Since this is the student's most difficult class, they should go to their
# professor's office hours for half the time they use to study to understand the material.

hardest_class_study_time = hardest_class_hours - hardest_class_office_hours
# This is the  number of hours the user is not using office hours, which will be used later.
print("You should dedicate", hardest_class_office_hours, "hours to visiting your professor's office hours.")
hardest_review = 100 - hardest_class_grade
# This will be used to calculate the percent of study
# time needed to review and practice problems.

hardest_review_percent = hardest_review / 100
# This equation turns the grade percentage into a decimal.
hardest_review_time = hardest_review_percent * hardest_class_study_time
# This will be the recommended number of hours for the user to review and practice problems.

print("Review and practice problems for at least", hardest_review_time, "hours.")

print("Brain break!")
number_1 = int(input("Guess a number 1 through ten that I may be thinking of: "))
print(number_1 > 7 or number_1 <= 2)
number_2 = int(input("Try another: "))
if number_2 <= 3 or number_2 == 8:
    print("Correct!")
elif number_2 == 4 or number_2 <= 7 and not number_2 == 10:
    print("So close!")
else:
    print("Wrong. Better luck next time.")

if number_1 < 3 and number_2 < 3:
    print("Both numbers were less than three.")
elif number_1 == 8 and number_2 == 8:
    print("Both numbers were 8 and correct.")

print("Now let's get back on task.")

easiest_class = input("What is your easiest class? ")
easiest_credits = int(float(input("How many credit hours is it? ")))
easiest_class_grade = int(float(input("Enter your grade: ")))
easiest_class_hours = int(float(input("Enter the number of hours per week you study for this class: ")))
easiest_class_total_time = easiest_class_hours * 2
# This equation represents the minimum number of hours recommended to spend out of class.

if easiest_class_grade == 100:
    print("Keep up the great work!")
if easiest_class_grade != 100:
    print("There is still room for improvement.")

print("You should dedicate at least", easiest_class_total_time, "hours outside of class to", easiest_class + ".")
easiest_class_office_hours = (easiest_class_hours / 4.00)
# Since this is the user's easiest class, they do not need
# to spend a significant amount of time using office hours.

easiest_class_study_time = easiest_class_hours - easiest_class_office_hours
# This is the number of hours the user is not using office hours which will be used later.
print("You should dedicate", easiest_class_office_hours, "hours to visiting your professor's office hours.")

hardest_easiest_total = 0
for x in range(1):
    hardest_easiest_total += hardest_class_total_time + easiest_class_total_time
    print(hardest_easiest_total)
    # This equation is the sum of hours dedicated so far to studying
    # for both the user's easiest and hardest classes.
    # The range is only one because it must only be executed one time.
x = 0
while x < 3:
    print(hardest_easiest_total)
    x = x + 1
print("Remember this number. "
      "This is the number of hours you have to study so far.")

print("So far you have", hardest_easiest_total, "out of a minimum of",
      min_study_time, "hours worth of studying per week to do.")

if (easiest_class_grade <= 80) and (hardest_class_grade <= 80):
    print("Amazing job keeping your grades at a B minus and above!")

answer1 = input("What is the modulus of 11 divided by 10? ")
correct_answer1 = 11 % 10
print("The answer is:", correct_answer1)
# Kat mentioned in class that if we could not figure out a way
# to implement modulus to demonstrate we know what it does.

print("This is because the modulus takes the remainder of the quotient.")

answer2 = input("What is 4 to the third power? ")
correct_answer2 = 4 ** 3
print("The answer is:", correct_answer2)


def add_numbers(number_1, number_2):
    print(number_1, "+", number_2, "=", number_1 + number_2)


def subtract_numbers(number_1, number_2):
    print(number_1, "-", number_2, "=", number_1 - number_2)


def main():
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter a second number: "))
    operator = input("Enter '+' to add and '-' to subtract. ")
    if operator == '+':
        add_numbers(number_1, number_2)
    elif operator == '-':
        subtract_numbers(number_1, number_2)
    else:
        print("Operator not valid.")


main()
# This was to implement the define function.

print("Okay, now back to your studying!")
number_of_classes1 = input("How many classes have you checked so far? ")

top_and_bottom_classes = [hardest_class, easiest_class]

favorite_class = input("What is your favorite class? ")
print("Let's see if favorite class discussed.")
print(favorite_class in top_and_bottom_classes)
# This checks to see if the class they input for
# favorite class is in the list.

print("We have covered the following classes: ")
for class_list1 in top_and_bottom_classes:
    print(class_list1)

print("Try to relax.")
total = 0
number_of_breaths = int(input("How many breaths of air would you like? "))
for x in range(number_of_breaths):
    for total in range(3, 0 - 1, -1):
        print(total)
    print("Breathe.")
