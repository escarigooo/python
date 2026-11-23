"""Write a program that prints, for each name in the list,
its letters separated by spaces — one name per line, exactly as the output below shows.
Start from the list given in the panel, and use this lecture’s nested for loops. No range is needed.

The output to produce:
>>> A d a
>>> G r a c e
>>> K e n
"""

names = ["Ada", "Grace", "Ken"]
for name in names:
    for letter in name:
        print(letter, end=" ")
    print()

# The program prints:
# A d a
# G r a c e
# K e n
