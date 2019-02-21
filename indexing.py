# In this exercise, you will write a program that gets
 # a specific character from a phrase entered by the user.

# Project Title:Indexing_challange
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in Python 3.7
# date 2019-02-20
# Project name: Strings
# Issues and concerns: none
# Problem domain Strings


def main():
    phrase = str(input("Enter a phrase "))
    sentence = 'You entered \"{0}\"' .format(phrase)
    print(sentence)
    location = int(input("Which charater would you like to see? "))
    letter = phrase[location - 1]
    print(letter)

main()
