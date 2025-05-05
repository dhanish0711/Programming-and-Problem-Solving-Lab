# Write a program to count the number of vowels using sets in a given string.

def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for char in str:
		if char in vowel:
			count += 1
	print(count)
str = input()
vowel_count(str)
