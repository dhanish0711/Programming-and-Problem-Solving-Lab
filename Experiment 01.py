# Write a program to calculate the area of a circle and print the result as shown in the displayed test cases.

radius = float(input("Enter the radius : "))
if 0.0 <= radius <= 100.0:
	area = 3.14 * radius * radius
	print("Area of circle = %.6f"%area)
else:
	print("Enter a positive value upto 100")
