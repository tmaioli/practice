# Project Title: Primes
# Version: 1.0
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in: Python 3.7
# date: 2019-02-20
# Project name:
# Issues and concerns: none
# Problem domain:

# Python program to check if the input number is prime or not

num = int(input("Enter a number: "))

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
