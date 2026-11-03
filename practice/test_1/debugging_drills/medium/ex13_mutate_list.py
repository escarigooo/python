"""EXERCISE 13 — Mutating list elements

Increase every temperature by one degree. Change the original list.

Expected output: [13, 16, 10]

Correct the program using indexes and explain why changing item is insufficient.
"""

temperatures = [12, 15, 9]

for item in temperatures:
    item = item + 1

print(temperatures)

