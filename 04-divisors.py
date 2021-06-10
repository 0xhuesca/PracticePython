
'''
https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Exercise 4 (and Solution)

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''


value = int(input("Please, enter a number: "))
i = 0
mylist=[]

while(i < value):
	i+=1
	if (value%i ==0):
		mylist.append(i)

print("The number " + str(value) + " is divible by " + str(mylist))




