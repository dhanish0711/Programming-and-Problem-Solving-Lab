# Write a Python program that prints prime numbers less than n which represents the upper limit.

n = int(input("Enter upper limit: "))
for num in range(2, n):
	is_prime = True
	for i in range(2, num):
		if num % i == 0:
			is_prime = False
			break
	if is_prime:
		print(num)
