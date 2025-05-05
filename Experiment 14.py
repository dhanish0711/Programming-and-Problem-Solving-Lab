# Write a Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid. If the digits are valid, the program generates all possible combinations of these three digits and prints them. Each combination is formed by arranging the digits in different orders. If the input is not valid (digits are not between 0 and 9), the program should display as "Invalid".

digit1 = input("digit1 (0-9): ")
digit2 = input("digit2 (0-9): ")
digit3 = input("digit3 (0-9): ")

if digit1.isdigit() and digit2.isdigit() and digit3.isdigit():
	num1, num2, num3 = int(digit1), int(digit2), int(digit3)
	if 0 <= num1 <= 9 and 0 <= num2 <= 9 and 0 <= num3 <= 9:
		print((num1), (num2), (num3), sep = "")
		print((num1), (num3), (num2), sep = "")
		print((num2), (num1), (num3), sep = "")
		print((num2), (num3), (num1), sep = "")
		print((num3), (num1), (num2), sep = "")
		print((num3), (num2), (num1), sep = "")
	else:
		print("Invalid")
else:
	print("Invalid")
