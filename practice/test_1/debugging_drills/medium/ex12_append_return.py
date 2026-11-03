"""EXERCISE 12 — append() return value

Build a list containing the integers 1, 2, and 3.

Expected output: [1, 2, 3]

Correct the program and explain what append() returns.
"""

numbers = []

for number in range(1, 4):
    numbers = numbers.append(number)

print(numbers)

