# Project Title:  Find e
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
# Keep your code dry. :)

'''
Find e to the Nth Digit -
Just like the previous problem, but with e instead of PI.
Enter a number and have the program generate e up to that many
decimal places. Keep a limit to how far the program will go.
'''

import math
E = math.e
print("This is the value of e ", E)

precision = int(input("Enter the precision of you you would like: "))

E = round(E, precision)
print(E)
