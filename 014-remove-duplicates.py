'''
https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first 
list minus all the duplicates.

'''
names = ["juan", "pedro", "natalie", "ivana", "lorenzo", "juan", "pepelu", "maria", "natalie", "kate"]

def _noduplicates_sets(a):
    ordered=set()
    for value in a:
        ordered.add(value)
    return print(ordered)

_noduplicates_sets(names)


def _noduplicates_list(b):
    names_b = set(b)
    names_b= list(names_b)
    return print(names_b)

_noduplicates_list(names)


