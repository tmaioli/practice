# Project Title: Grades
# Version: 1.0
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in Python 3.7
# date 2019-02-20
# Project name: grades
# Issues and concerns: none
# Problem domain "dictonary problem"

scores = []
print("Welcome to the grading program.")
english = int(input("English grade: "))
math = int(input("Math grade: "))
globals = int(input("Enter global: "))
art = int(input("Enter art: "))
music = int(input("Enter music: "))

def sum():
    sum_of_grades = (english + math + globals + art + music)

def find_average(english, math, globals, art, music):
    average = (english + math + globals + art + music) / 5
    return average

print((english + math + globals + art + music))
# print("your average is: ", (sum_of_grades/5))

find_average()
