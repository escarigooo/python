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

# Answer: 10 3 9 — one line. The loop stops on the 9 because values[3] > 7,
# so break leaves before i = i + 1 runs, and the 9 never joins the total
# (3 + 5 + 2 = 10).
# i is therefore 3, and values[3] is the 9 that stopped it.

# Concepts: while driven by an index, break inside an if (week 8) · the
# accumulator and the loop variable read after the loop (week 6) · len and
# indexing a list (week 4).
