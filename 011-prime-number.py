
'''
Exercise 11 (and Solution)

https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html


Ask the user for a number and determine whether the number is prime or not. (For those who 
have forgotten, a prime number is a number that has no divisors.). You can (and should!) use 
your answer to Exercise 4 to help you. Take this opportunity to practice using functions, 
described below.

'''

'''
user_number=input("Tnter a number: ")

if user_number.isnumeric() == True:
    if (int(user_number)%2 == 0):
        print("The number is not prime. \n")
    else:
        print("The number is prime. \n")
else:
    print("Enter a number... \n")

'''

def _prime(num):
    if num.isnumeric() == True:
        if (int(num)%2 == 0):
            print("The number is not prime. \n")
        else:
            print("The number is prime. \n")
    else:
        print("Enter a number... \n")
    return 0

_prime(input("Enter a number:"))


