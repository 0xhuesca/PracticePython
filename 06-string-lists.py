
'''

https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html



Exercise 6 (and Solution)

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

'''


value = str(input("Enter a beautiful string: "))

revvalue=value[::-1]

if(value == revvalue):
	print("The message is palindrome")

else:
	print("the message is not palindrome")




