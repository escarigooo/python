"""EXERCISE 10 — Updating a counter

Count how many values are even.

For numbers = [3, 8, 4, 7, 10]
Expected output: Even values: 3

Correct the program and explain the counter update.
"""

numbers = [3, 8, 4, 7, 10]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count + 1

print(f"Even values: {even_count}")

