
'''
https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a 
new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


'''

import string
import random

lenght = int(input("Please enter the lenght of the password: "))

def _generator(A):
    passwd=""
    mylist= [string.ascii_letters, string.punctuation, string.digits]
    for i in range(A):
        module= i % 3
        #module = random.choice(i % 3)
        passwd+=random.choice(mylist[module])
        
    return passwd

print("The password is: " + str(_generator(lenght)))





'''
for a in range (lenght):
    mod=a%3
    print( str(a) + ":"+ str(mod))
'''