"""
Write a Python program to print the following pattern.

Sample Input and Output:
Enter a number : 6
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

num = int(input("Enter a number : "))
for i in range(num, 0, -1):
	print("* " * i)
