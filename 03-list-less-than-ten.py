
'''

https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html


Exercise 3 (and Solution)

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

mylist = []


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Execise 3.2
#for value in a:
#	if value < 5:
#		mylist.append(value)

#print(mylist)

#Execise 3.3
user_value = int(input("Enter a max value: "))
for value in a:
	if (value < user_value):
		mylist.append(value)

print(mylist)

