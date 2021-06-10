'''
Exercise 13 (and Solution)
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Write a program that asks the user how many Fibonnaci numbers to 
generate and then generates them. Take this opportunity to think 
about how you can use functions. Make sure to ask the user to enter 
the number of numbers in the sequence to generate.(Hint: 
The Fibonnaci seqence is a sequence of numbers where the next number
 in the sequence is the sum of the previous two numbers in the 
 sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

F[0]=0
F[1]=1
F_{n}=F_{{n-1}}+F_{{n-2}} (per ogni n>1)

'''


num = int(input("How many numbers that generates?: "))

def fibo(a):
    list=[]
    i=1
    s=0
    if a<=0:
        list=[0]
    elif a==1:
        list=[1]
    elif a == 2:
        while s < a:
            list.extend(fibo(1))
            s+=1
    elif a > 2:
        list.extend(fibo(2))
        while i < (a-1):
            list.append(list[i]+list[i-1])
            i+=1
    return list

print(fibo(num))


