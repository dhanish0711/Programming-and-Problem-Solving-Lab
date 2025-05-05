# Write a Python program to find whether a given string is a palindrome or not.

s = input()
if s == s[::-1]:
	print("palindrome")
else:
	print("not a palindrome")
