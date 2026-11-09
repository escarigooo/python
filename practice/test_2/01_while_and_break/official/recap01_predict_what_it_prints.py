"""Recap 1 · Predict what it prints

Read the program below and write exactly what it prints — every line, in order. On paper, before any run. Then run it and compare.
"""
values = [3, 5, 2, 9, 4]
total = 0
i = 0
while i < len(values):
    if values[i] > 7:
        break
    total = total + values[i]
    i = i + 1
print(total, i, values[i])
