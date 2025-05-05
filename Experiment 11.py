# Write a Python program that prompts the user to input a date (year, month, and day) and checks if it is a valid date. If the entered date is valid, the program should increment the date by one day and display the incremented date. The program should take into account leap years when determining the number of days in February.

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
month_days = [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12 or day < 1 or day > month_days[month - 1]:
	print("invalid")
else:
	print("valid")
	day += 1
	if day > month_days[month - 1]:
		day = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
	print(f"incremented date: {year}-{month:02d}-{day:02d}")
