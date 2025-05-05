# Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.

sentence = input()
modified_sentence = ""
for char in sentence:
	if char.isalnum() or char.isspace():
		modified_sentence += char
print(modified_sentence)
