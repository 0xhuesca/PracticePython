
'''
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.

'''


user_resp = input("Enter a beautiful frase: ")

def _reversing_string(a):
    resp_user=a.split()
    resp_user.reverse()
    resp_user=":) ".join(resp_user)
    return print(resp_user)
_reversing_string(user_resp)

