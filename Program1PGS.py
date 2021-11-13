# program: grading system
# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.5           79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed
grade = round(float(input("Enter your Grade: ")))

if grade > 100:
    print("There is no such grade that exceeds the maximum grade of 100.")

elif grade >=97 and grade <=100:
    print("Grade/Mark: 1.0")
    print("Description: Excellent")

elif grade >=94 and grade <=96:
    print("Grade/Mark: 1.25")
    print("Description: Excellent")

elif grade >=91 and grade <=93:
    print("Grade/Mark: 1.5")
    print("Description: Very Good")

elif grade >=88 and grade <=90:
    print("Grade/Mark: 1.75")
    print("Description: Very Good")

elif grade >=85 and grade <=87:
    print("Grade/Mark: 2.0")
    print("Description: Good")

elif grade >=82 and grade <=84:
    print("Grade/Mark: 2.25")
    print("Description: Good")

elif grade >=79 and grade <=81:
    print("Grade/Mark: 2.5")
    print("Description: Satisfactory")

elif grade >=76 and grade <=78:
    print("Grade/Mark: 2.75")
    print("Description: Satisfactory")

elif grade ==75:
    print("Grade/Mark: 3.00")
    print("Description: Passing")

elif grade >=65 and grade <=74:
    print("Grade/Mark: 5.0")
    print("Description: Failure")

else:
    print("Your grade is either Inc. means Incomplete, W means Withdrawn, or D means Dropped.")
