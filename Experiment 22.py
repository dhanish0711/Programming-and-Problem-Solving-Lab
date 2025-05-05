"""
Take an integer n from the user. Your task is to Write a program to find out the sum of the digits of the given number using the process of recursion. Print the result as shown in the Test cases. 
The program defines the Sumof() function.
In the main program it takes the input n and sends it to the Sumof() function.
The Sumof() function contains base and recursive criterion.
"""

def Sumof(n):
	sum = 0
	while n != 0:
		r = int(n % 10)
		sum = sum + r
		n = int(n / 10)
	return sum
a = int(input())
b = Sumof(a)
print(f"{b}")
