"""The program should print the sum of each row of the matrix —
6, then 15, then 24, one line per row.
It runs and raises nothing, yet every line it prints is wrong.
Find every line to blame, say what each one does to the sums, and write the fixes.
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in range(3):
    total = 0  # fix 1: moved inside the outer loop, so each row starts its own sum
    for col in range(3):
        total = total + m[row][col]  # fix 2: the two indices were swapped
    print(total)

# Two lines were to blame, and fixing only one still prints three
# wrong lines. As written the program printed 12, 27, 45.
# (1) total = 0 sat before BOTH loops, so the sum never started again
#     for a new row — each line carried everything before it.
#     With only this fixed: 12, 15, 18 — the column sums, neat and wrong.
# (2) The body read m[col][row] — the indices swapped, so what was
#     summed row by row was really the columns.
#     With only this fixed: 6, 21, 45 — and the FIRST line is right,
#     which is the deeper trap.

# Fixed, the program prints:
# 6
# 15
# 24
