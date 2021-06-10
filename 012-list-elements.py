'''
Exercise 12 (and Solution)
https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.

'''

a = [5, 10, 15, 20, 25, 50, 23]

if (len(a)!=0):
    _list=[]
    if(len(a)>1):
        _list.append(a[0])
        _list.append(a[len(a)-1])
        print(_list)
    else:
        _list.append(a[0])
        print(_list)
else:
    print("List is null")

