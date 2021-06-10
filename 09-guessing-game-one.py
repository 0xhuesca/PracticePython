'''
https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Exercise 9 (and Solution)

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user 
input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''

import random as  ran

_range=[]
for i in range(2, 9):
    _range.append(i)

print(_range)
while 1:
    number = ran.randint(2, 9) # generate a random number from 2 to 9, including both numbers#
    user_input = input("A random number was generated, enter you criteria between 2 and 9: \n")

    if user_input.isnumeric() == True:
        if user_input == number:
            print("you number %d was right" % (int(user_input)))
        elif ((int(user_input) < number) and (int(user_input) in _range)):
            print("you number %d was too low \n" % (int(user_input)))
        elif ((int(user_input) > number) & (int(user_input) in _range)):
            print("you number %d was too high \n" % (int(user_input)))
        else:
            print("Entered value %d was out of range \n" % (int(user_input)))
    elif user_input == "exit" :
        break
    else:
        print("Enter a valid value \n")
    
print("Thanks for gaming... \n\n")