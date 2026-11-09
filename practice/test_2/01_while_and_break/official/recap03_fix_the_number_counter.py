"""Recap 3 · Debug

The program should ask for numbers until the user types 0, then print how many numbers were typed and their sum. It runs, but it never stops — not even after a 0. Find every line to blame, say why each one keeps the loop going, and write the fixes.

It loops forever on purpose — run it only with the Stop button at hand.
"""
total = 0
count = 0
n = input("Number: ")
while n != 0:
    total = total + int(n)
    count = count + 1
n = input("Number: ")
print(count, total)
