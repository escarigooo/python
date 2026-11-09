"""The program should print the sum of each row of the matrix —
6, then 15, then 24, one line per row.

It runs and raises nothing, yet every line it prints is wrong.
Find every line to blame, say what each one does to the sums,
and write the fixes.
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for row in range(3):
    for col in range(3):
        total = total + m[col][row]
    print(total)
