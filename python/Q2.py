#A school needs to check if a student has passed or failed based on their marks. If marks are greater than or equal to 50, the student passes; otherwise, they fail. Write a program that outputs whether the student passed or failed

marks = float(input("Enter student's marks: "))
if marks >= 50:
    print("Passed")
else:
    print("Failed")
