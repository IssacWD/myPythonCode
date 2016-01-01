# Create a list of 99 boolean elements with value False
isCovered = 99 * [False]
endOfInput = False
while not endOfInput:
	# Read numbers as a string from the console
	s = input("Enter a line of numbers separated by spaces: ")
	items = s.split() # Extract items from the string
	lst = [eval(x) for x in items] # Cover items to numbers

	for number in lst:
		if number == 0:
			endOfInput = True
		else:
			# Mark its corresonding element covered
			isCovered[number - 1] = True

# Check whether all numbers (1 to 99) are covered
allCovered = True
for i in range(99):
	if not isCovered[i]:
		allCovered = False
		break

# Display result
if allCovered:
	print("The tickets cover all numbers.")
else:
	print("The tickets does not cover all numbers.")