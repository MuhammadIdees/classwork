# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:47:40 2019

@author: M IDREES
"""

#Question_23
"""Write a function that returns the maximum number between two numbers"""

def maximum(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2
    
#Question_24
"""
Write a funciton check_num
    •If the number is divisible by 3, it should return “Divisible by 3”. 
    •If it is divisible by 5, it should return “Divisible by 5”. 
    •If it is divisible by both 3 and 5, it should return “Divisible by both”. 
    •Otherwise, it should return the same number.
"""

def check_num(number):
    if ((number % 3 == 0) and (number % 5 == 0)):
        print("Divisible by both")
    elif (number % 5 == 0):
        print("Divisible by 5")
    elif (number % 3 == 0):
        print("Divisible by 3")
    else:
        return number
    
#Question_25
"""
Write a function called showNumbers that takes a parameter called limit. 
It should print all the numbers between 0 and limit

"""

def showNumber(limit):
    for i in range(limit):
        print(i)

#Question_26
"""
Write a Python program which accepts the radius of a circle 
from the user and compute the area of circle

"""
radius = float(input("Enter the radius of circle: "))

print ("Area of circle: ", 3.1417*radius*radius)        

#Question_27
"""
Write a function that returns the sum of multiples of 
3 and 5 between 0 and limit (parameter). For example, if limit is 20, 
it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

"""
def blahblah(limit):
    sum = 0;
    for i in range(limit + 1):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum +=i
    return sum

#Question_28
"""
Ques: 28	Write a function called show_stars(rows). If rows are 5, 
it should print the following: 
* 
** 
*** 
**** 
*****

"""
def show_stars(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*", end="")
        print()

#Question_29
"""
Write a function that prints all the prime numbers 
between 0 and limit where limit is a parameter.
 
"""
def prime(limit):
    for i in range(2, limit+1):
        isPrime = True
        
        for j in range (2, i):
            if (i % j == 0):
                isPrime = False
        
        if isPrime:
            print(i)
            
#Question_31
"""
Write a program that prints first and last name in revesrse order

"""
first_name = input('Enter your first name: ')
last_name  = input('Enter your last name: ')

print(last_name + " " + first_name)

#Question_32
"""
Write a program to tell user if he has entered an even or odd number

"""
number = int(input('Input a number: '))

if number % 2 == 0:
    print ("The entered number is even")
else:
    print ("The entered number is odd")
    
#Question_33
"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

"""
number = int(input("Please input a number: "))

number += (number*10 + number) + (number*100 + number*10 + number)

print(number)

#Question_34
"""
Program to tell if the given word has vowel or not

"""
word = "Pakistan"

if (word.find("a") < 0 or word.find("e") < 0 or word.find("o") < 0 or word.find("i") < 0 or word.find("u") < 0):
    print ("The word has vowel")
else:
    print ("No vowel present in word")
    
#Question_35
"""
Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero.
 
"""

num1 = 1
num2 = 2
num3 = 3

if (num1 == num2 or num2 == num3):
    print(0)
else:
    print(num1 + num2 + num3)

#Question_36
"""
Write a Python program that will return true if the two given 
integer values are equal or their sum or difference is 5. 

"""
def gaga(num1, num2):
    if (num1 == num2 or (num1 + num2 == 5) or num1 - num2):
        return True
    else:
        return False

#Question_37
"""
Write a Python program to solve (x + y) ^(z)

"""
x = 1
y = 2
z = 3

print(pow((x + y), z))



