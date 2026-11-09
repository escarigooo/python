"""Exercise 4 · Fix the program

This program should stop at the first zero.
It runs and raises nothing, yet it reports both zeros.
Say what is missing, where it belongs, and write the fix.
Everything in it is this lecture’s material.
"""
values = [4, 0, 7, 0]
for v in values:
    if v == 0:
        print("found zero")  # now prints once
        break  # the missing line: inside the if, right after the print
