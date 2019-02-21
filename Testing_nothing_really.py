'''


x,y,z =100, 200,300

print(x,y,z)
del x
print(y,z)

# it is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1,2,3]
x = [a, n]
print(x)
print(x[0])
z = len(x)
print(z)



# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
print(long_word)
length = len(long_word)

for letter in long_word:
        print(letter)
        First = long_word.index("t")
print("First letter found at ", First + 1)

z=length - First

for letter in long_word[z + 1:]:
        print(letter)
        second = long_word.index("t")
print("Second letter found at ", second + 1)

print(long_word[First:second])
'''
