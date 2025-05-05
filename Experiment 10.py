"""
Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system:

A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: Below 60

The program should display the average marks up to 2 decimal places and the assigned grade.
"""

subject1 = float(input("subject 1: "))
subject2 = float(input("subject 2: "))
subject3 = float(input("subject 3: "))
subject4 = float(input("subject 4: "))
subject5 = float(input("subject 5: "))

average = (subject1 + subject2 + subject3 + subject4 + subject5) / 5.0
print("Average Marks: %.2f" %(average))

if average <= 100 and average >= 90:
	print("Grade: A")
elif average <= 89 and average >= 80:
	print("Grade: B")
elif average <= 79 and average >= 70:
	print("Grade: C")
elif average <= 69 and average >= 60:
	print("Grade: D")
elif average <= 60 and average >= 0:
	print("Grade: F")
