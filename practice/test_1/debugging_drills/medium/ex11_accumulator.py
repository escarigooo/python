"""EXERCISE 11 — Accumulator placement

Add all prices without using sum().

For prices = [4.5, 3.0, 2.5]
Expected output: Total: 10.0

Correct the program and explain where total must be initialized.
"""

prices = [4.5, 3.0, 2.5]

for price in prices:
    total = 0
    total = total + price

print(f"Total: {total}")

