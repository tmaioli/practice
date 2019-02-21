# Project Title: Count Letters
# Version: 1.0
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in: Python 3.7
# date: 2019-02-20
# Project name: count letters
# Issues and concerns: none
# Problem domain: length and count
# Keep your code dry. :)


# for letters: "e" and "a" in random_tip
# [ ] print letter counts
# [ ] BONUS: print which letter is most frequent

random_tip = "none"


from collections import Counter
import string

random_tip = input("Enter a sentence ")
x = random_tip


get_length = int(len(random_tip))

print("Your String is this many charaters", get_length)

x = Counter(x)
print("Here are your letter counts")
print(x)
