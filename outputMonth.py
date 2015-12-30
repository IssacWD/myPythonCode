# Print the calendar for a month in a year
def printMonth(year,month):
	# Print the Title of month
	printMonthTitle(year,month)
	# Print the body of this month
	printMonthBody(year,month)

# Peint the Title :e.g., May 1999
def printMonthTitle(year,month):
	print("  ",getMonthName(month),"  ",year)
	print("====================================")
	print(" Sun Mon Tue Wed Thu Fri Sat")

# Print month body
def printMonthBody(year,month):
	# Get start day of the week for the date in the month
	startDay = getStartDay(year,month)
	# Get number of days in month
	numberOfDaysInMonth = getNumberOfDaysInMonth(year,month)
	# Pad space before the first day of the month
	for i in range(0,startDay):
		print("   ",end = " ")
	for i in range(1,numberOfDaysInMonth + 1):
		print(format(i,"4d"),end = " ")
		if (i + startDay) % 7 == 0:
			print()# Jump to the new line

# Get the name of month
def getMonthName(month):
	if month == 1:
		monthName = "January"
	elif month == 2:
		monthName = "February"
	elif month == 3:
		monthName = "March"
	elif month == 4:
		monthName = "April"
	elif month == 5:
		monthName = "May"
	elif month == 6:
		monthName = "June"
	elif month == 7:
		monthName = "July"
	elif month == 8:
		monthName = "August"
	elif month == 9:
		monthName = "September"
	elif month == 10:
		monthName = "October"
	elif month == 11:
		monthName = "November"
	elif month == 12:
		monthName = "December"
	return monthName

# Get start day of month/1/year
def getStartDay(year,month):
	START_DAY_FOR_JAN_1_1800 = 3
	# Get total number of days from 1/1/1800 to month/1/year
	totalNumberOfDays = getTotalNumberOfDays(year,month)
	return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7

# Get the totla number of days since 1/1/1800
def getTotalNumberOfDays(year,month):
	total = 0

	# Get the total days from 1/1/1800 to 1/1/year
	for i in range(1800,year):
		if isLeapYear(i):
			total = total + 366
		else:
			total = total + 365
	# Add days from Jan to the month prior to the calendar month
	for i in range(1,month):
		total = total + getNumberOfDaysInMonth(year,i)

	return total
# Get the number of day in month
def getNumberOfDaysInMonth(year,month):
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
		return 31
	if (month == 4 or month == 6 or month == 9 or month == 11):
		return 30
	if month == 2:
		if isLeapYear(year):
			return 29
		else:
			return 28

# Determine the year
def isLeapYear(year):
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
	# Get input
	year = eval(input("Enter the year :"))
	month = eval(input("Enter the month :"))
	printMonth(year,month)
# Call the main
main()
