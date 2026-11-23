"""Two nested loops and two appends: a row is built, then the row is appended to the matrix."""

# the data
matrix = []

# the work
for i in range(2):
    row = []
    for j in range(2):
        row.append(j)
    matrix.append(row)

# the answer
print(matrix)
