# coding=utf-8
#********************************************************
# > OS     : Linux CentOS 6.5 / Windows
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2015年12月31日 
#********************************************************
def main():
	# Prompt the user to enter a string
	s = input("Enter a string :").strip()

	if isPalindrome(s):
		print(s," is a palindrome")
	else:
		print(s," is not a palindrome")

# Check the string
def isPalindrome(s):
	# The index of the first character in the string
	low = 0
	# The index of the last character in the string
	high = len(s) - 1

	while low < high:
		if s[low] != s[high]:
			return False

		low += 1
		high -= 1
	return True

main()
