"""EXERCISE 14 — Removing while iterating

Remove every negative value from the list.

Expected output: [4, 7]

The current program sometimes skips neighbouring negative values. Correct it by
iterating over a copy and explain why that works.
"""

values = [-2, -3, 4, -5, -6, 7]

for value in values:
    if value < 0:
        values.remove(value)

print(values)

