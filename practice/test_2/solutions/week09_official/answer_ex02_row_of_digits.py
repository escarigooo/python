"""Write a program that prints the four rows below, exactly as the output shows:
row 1 shows one 1, row 2 shows two 2s, and so on up to four 4s.
Use this lecture’s nested for loops.

The output to produce:
>>> 1
>>> 22
>>> 333
>>> 4444
"""

for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

# The program prints:
# 1
# 22
# 333
# 4444
