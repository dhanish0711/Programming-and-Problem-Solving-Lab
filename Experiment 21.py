# Write a program to print the sum of digits of a number.

num = input("num: ")
sum_digits = 0
for digit in num:
	sum_digits += int(digit)
print("sum:", sum_digits)
