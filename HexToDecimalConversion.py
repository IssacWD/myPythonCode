# coding=utf-8
#********************************************************
# > OS     : Linux CentOS 6.5 / Windows
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2015年12月31日 
#********************************************************
def main():
	print("====================================")
	# Prompt user to enter a string
	d = eval(input("Hex To Decimal: 1\nDecimal To Hex: 2\n Select : "))
	if d == 1:
		s = input("Enter a string, hex :").strip()
	elif d == 2:
		s = input("Enter a number, decimal :")
	elif d != 1 or d != 2:
		print("Please rechoose 1 or 2 \n")
		main()

	if d == 1 and checkHexOrDecimal(s):
		print("You input a hex number:",s)
		print("The decimal value for hex number ",s," is ",hexToDecimal(s),"\n")
	elif d == 2:
		print("You input a decimal number:",s)
		print("The hex value for decimal number ",s," is ",decimalToHex(s),"\n")
	elif checkHexOrDecimal(s) == False:
		print("The string is not a hex or decimal number, please reinput a string\n")
		main()

	cont = input("Do you want to continue? (yes:y no:n)\nSelect :")
	if cont == 'y':
		main()

def checkHexOrDecimal(s):
	countNumber = 0
	countAtoF = 0
	countElse = 0
	for i in range(0,len(s) - 1):
		asc = ord(s[i])
		if 48 <= asc <= 57:
			countNumber += 1
		elif 65 <= asc <= 70 or 97 <= asc <= 102:
			countAtoF += 1
		else:
			countElse += 1

	if countElse != 0:
		return False
	else:
		return True

def hexToDecimal(s):
	decimalValue = 0
	for i in range(len(s)):
		hexChar = s[i]
		decimalValue = decimalValue * 16 + charHexToDecimal(hexChar)
	return decimalValue

def decimalToHex(s):
	hexValue = ''
	hexValue2 = ''
	remaind = int(s)
	while remaind != 0:
		decimalChar = remaind % 16
		remaind = remaind // 16
		hexValue = hexValue + charDecimalToHex(decimalChar)
	
	for i in range(len(hexValue),0,-1):
		hexValue2 = hexValue2 + hexValue[i-1]

	return hexValue2

def charHexToDecimal(hexChar):
	if hexChar == '0':
		return 0
	elif hexChar == '1':
		return 1
	elif hexChar == '2':
		return 2
	elif hexChar == '3':
		return 3
	elif hexChar == '4':
		return 4
	elif hexChar == '5':
		return 5
	elif hexChar == '6':
		return 6
	elif hexChar == '7':
		return 7
	elif hexChar == '8':
		return 8
	elif hexChar == '9':
		return 9
	elif hexChar == 'A' or hexChar == 'a':
		return 10
	elif hexChar == 'B' or hexChar == 'b':
		return 11
	elif hexChar == 'C' or hexChar == 'c':
		return 12
	elif hexChar == 'D' or hexChar == 'd':
		return 13
	elif hexChar == 'E' or hexChar == 'e':
		return 14
	elif hexChar == 'F' or hexChar == 'f':
		return 15

def charDecimalToHex(decimalChar):
	if decimalChar == 1:
		return '1'
	elif decimalChar == 2:
		return '2'
	elif decimalChar == 3:
		return '3'
	elif decimalChar == 4:
		return '4'
	elif decimalChar == 5:
		return '5'
	elif decimalChar == 6:
		return '6'
	elif decimalChar == 7:
		return '7'
	elif decimalChar == 8:
		return '8'
	elif decimalChar == 9:
		return '9'
	elif decimalChar == 10:
		return 'A'
	elif decimalChar == 11:
		return 'B'
	elif decimalChar == 12:
		return 'C'
	elif decimalChar == 13:
		return 'D'
	elif decimalChar == 14:
		return 'E'
	elif decimalChar == 15:
		return 'F'
	
main()


