"""
Implement a Python program using a class named Complex to perform operations on complex numbers. The class has the following methods:
initComplex(): A method that takes user input for the real and imaginary parts to initialize a complex number.
display(): A method that displays the complex number in the form "a + bi".
sum(): A method that computes the sum of two complex numbers and stores the result in the current instance.

The program creates three instances of the Complex class, initializes two complex numbers, displays them, computes their sum, and displays the result.
"""

class Complex ():
	def __init__(self):
		self.real = 0
		self.imaginary = 0
	def initComplex(self):
		self.real = int(input("Real Part: "))
		self.imaginary = int(input("Imaginary Part: "))
	def display(self):
		if self.imaginary >= 0:
			print(f"{self.real}+{self.imaginary}i")
		else:
			print(f"{self.real}+{self.imaginary}i")
	def sum(self, c1, c2):
		self.real = c1.real + c2.real
		self.imaginary = c1.imaginary + c2.imaginary

c1 = Complex()
c2 = Complex()
c3 = Complex()
print("complex number 1")
c1.initComplex()
c1.display()
print("complex number 2")
c2.initComplex()
c2.display()
print("Sum:", end = " ")

c3.sum(c1,c2)
c3.display()
