"""
# Project Title: Count Letters
# Version: 1.0
# Instructions:
# Prerequisites: Python 3
# Built with: Atom text editor
# Thomas Maioli
# coded in: Python 3.7
# date: 2019-02-20 and 2026-07-07
# Project name: count letters
# Issues and concerns: none
# Problem domain: length and count
# [ ] print letter counts
# [ ] BONUS: print which letter is most frequent

Enter a sentence: the cat ran fast
Your String is this many charaters 16
Here are your letter counts
Counter({'t': 3, ' ': 3, 'a': 3, 'h': 1, 'e': 1, 'c': 1, 'r': 1, 'n': 1, 'f': 1, 's': 1})

=== Code Execution Successful ===

"""

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
