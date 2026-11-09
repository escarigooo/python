"""The table was computed by hand: in each row, the last value claims to be the sum of the three before it.
One claim is wrong. Write the program that checks every row and prints the verdicts,
exactly as the output shows — with this lecture’s nested for loops.

The output to produce:
>>> row 0 ok
>>> row 1 WRONG
>>> row 2 ok
"""

table = [[7, 2, 9, 18], [4, 1, 5, 11], [3, 8, 6, 17]]
for i in range(3):
    total = 0
    for j in range(len(table[i])-1):
        total = total + table[i][j]
    if total == table[i][len(table[i])-1]:
        print("row", i, "ok")
    else:
        print("row", i, "WRONG")

# The program prints:
# row 0 ok
# row 1 WRONG
# row 2 ok

# The inner loop, `for j in range(len(table[i])-1)`, iterates over all elements
# of the inner list except the last one, which represents the claimed sum.
# `table[i][len(table[i])-1]` accesses the last element of the inner list.
#
# Notice the difference:
# - When used inside `range()`, `len(table[i])-1` is the **stop value**,
# which is excluded from the generated sequence.
# - When used as an index, `len(table[i])-1` identifies the **last element** of the list,
# since indexing starts at 0.