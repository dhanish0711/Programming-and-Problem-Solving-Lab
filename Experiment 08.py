# Write a Python program to perform union, intersection and difference operations on Set A and Set B.

a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations
print("Union: ", A | B)
print("Intersection: ", A & B)
print("Difference: ", A - B)
