"""Write a program that prints a 4-by-4 block of # characters, exactly as the output below shows.
Use this lecture’s nested for loops.

The output to produce:
>>> ####
>>> ####
>>> ####
>>> ####
"""

for i in range(4):
    for j in range(4):
        print("#", end="")
    print()

# The program prints:
# ####
# ####
# ####
# ####
