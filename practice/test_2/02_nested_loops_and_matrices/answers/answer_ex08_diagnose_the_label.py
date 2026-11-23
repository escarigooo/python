"""This program should print three rows of stars,
each ending with its own number — row 0, row 1, row 2.
It runs and raises nothing, yet all three end with the same number.
Find the line to blame, explain what it does, and write the fix.
"""

for i in range(3):
    for j in range(2):  # the fix: the inner loop gets its own name
        print("*", end="")
    print(" row", i)

# The line to blame was the inner for reusing the name i: the outer
# counter was overwritten before the label printed, so every row
# ended with the inner loop's last value, 1. The outer loop still ran
# three times, because its sequence was fixed when the loop started.

# Fixed, the program prints:
# ** row 0
# ** row 1
# ** row 2
