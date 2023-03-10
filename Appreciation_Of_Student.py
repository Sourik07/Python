print("Enter details of Student:-\n")
#Number of S grades
grade=int(input("number of S grades: "))
if grade<0:
    print("Invalid Input!!")
#Total attendance in (%)
attendance=int(input("Percentage of Attendance: "))
if attendance<0:
    print("Invalid Input!!")
# Participation in sports activity in a semester
sports=int(input("Participation in sports activity in a semester: "))
if sports<0:
    print("Invalid input!!")
if grade>=3 and attendance>=90 and sports>=2:
    print("Excellent")
elif grade>=3 and attendance>=90:
    print("Very Good")
elif grade>=3 and sports>=2:
    print("Good")