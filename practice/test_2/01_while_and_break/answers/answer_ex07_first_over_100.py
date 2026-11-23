"""Exercise 7 · The first number over 100

Write the loop that prints the first number over 100 in the list — that number and nothing after it.
Start from the list given in the panel. Use this lecture’s break, inside week 6’s for.

>>> 120
"""
values = [40, 80, 120, 200]
for v in values:
    if v > 100:
        print(v)  # 120
        break
