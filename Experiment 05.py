# Write a Python program to find the roots of a quadratic equation by taking the coefficients from the user.

import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminant = b ** 2 - 4 * a * c
if discriminant >= 0:
	root1 = (-b + math.sqrt(discriminant)) / (2 * a)
	root2 = (-b - math.sqrt(discriminant)) / (2 * a)
	if discriminant == 0:
		print("The root is: {:.2f}".format(root1))
	else:
		print("The roots are: {:.2f} and {:.2f}".format(root1, root2))
else:
	real_part = -b / (2 * a)
	imag_part = math.sqrt(abs(discriminant)) / (2 * a)
	print("The roots are: {:.2f}+{:.2f}j and {:.2f}-{:.2f}j".format(real_part, imag_part, real_part, imag_part))
