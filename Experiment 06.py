# Write a Python program to find the largest of three numbers.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
	largest_number = num1
elif num2 >= num1 and num2 >= num3:
	largest_number = num2
else:
	largest_number = num3
print("Largest number:", largest_number)
