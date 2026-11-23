"""This program should print a 3-by-3 grid of stars.
It runs and raises nothing, yet everything comes out on a single line.
Find the line to blame, explain when it runs, and write the fix.
Everything in it is this lecture’s material.
"""

for i in range(3):
    for j in range(3):
        print("*", end="")
    print()  # the fix: indented one level, so it runs once per outer step

# The line to blame was the bare print() outside both loops: it ran
# once, after everything, so the rows never broke and the program
# printed ********* on a single line.

# Fixed, the program prints:
# ***
# ***
# ***
