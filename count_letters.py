'''
# for letters: "e" and "a" in random_tip
# [ ] print letter counts
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"

'''

from collections import Counter
import string

random_tip = input("Enter a sentence ")
x = random_tip


get_length = int(len(random_tip))

print("Your String is this many charaters", get_length)

x = Counter(x)
print(x)
