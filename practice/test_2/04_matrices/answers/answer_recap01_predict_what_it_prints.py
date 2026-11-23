"""Read the program below and write exactly what it prints — every line, in order.
On paper, before any run. Then run it and compare."""

M = [[1, 2], [3, 4], [5, 6]]
total = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        if i == j:
            M[i][j] = 0
        total = total + M[i][j]
print(M)                         # [[0, 2], [3, 0], [5, 6]]
print(total, len(M), len(M[0]))  # 16 3 2
