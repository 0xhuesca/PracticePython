# Practice Python Solution 
#
# URL = https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#
# Exercise 2:
#
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the 
user. Hint: how does an even / odd number react differently when divided by 2?
#
# Solution:

try:
	num = int(input("Please enter the number to be valuated: "))
	if (num%2 != 0):
		print("The number " + str(num) + " is an even number.")
	elif (num%4 == 0):
		print("The number " + str(num) + " is multiple of 4.")
	else:
		print("The number " + str(num) + " is a odd number.")
except:
	print("Error...")

