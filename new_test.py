# Project Title:  find len of names and other random messing around
# Version: 1.0
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in: Python 3.7
# date:
# Project name:
# Issues and concerns: none
# Problem domain:
# Keep your code dry. :)


#New_test
#logical operator

'''
num1 = 400
num2 = 200
num3 = 300
result = (num1 >= num2) or (num1 == num3)# or any of the other booleans
print(result)


#conditionals

big = "p"
small = "p"

if big > small:
    print("bigger")
elif big < small:
    print("smaller")
#elif big == small:
#    print("equal")

else:
     print("What?")


print("Enter a number : ")
number = int(input())

if number < 0:
    print("Number is '-'")
elif number == 0:
    print("zero")
else:
    print("+")
'''



companies = ["apple","xerox","Netflix", "Wegmans"]
for names in companies:
    print(names, (len(names)))
