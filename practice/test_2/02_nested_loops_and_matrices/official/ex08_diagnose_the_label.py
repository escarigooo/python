"""This program should print three rows of stars,
each ending with its own number — row 0, row 1, row 2.
It runs and raises nothing, yet all three end with the same number.
Find the line to blame, explain what it does, and write the fix.
"""

for i in range(3):
    for i in range(2):
        print("*", end="")
    print(" row", i)
