"""Write a program that prints exactly the triangle below:
five stars on the first row,
one on the last,
each row one star shorter than the one above.
Use this lecture’s nested for loops.

The output to produce:
>>> *****
>>> ****
>>> ***
>>> **
>>> *
"""

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# The program prints:
# *****
# ****
# ***
# **
# *

# A second correct answer keeps the outer loop counting up
# and shortens the row instead:
# for i in range(5):
#     for j in range(5 - i):
#         print("*", end="")
#     print()
