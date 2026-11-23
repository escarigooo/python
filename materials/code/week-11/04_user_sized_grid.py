"""A grid of zeros in the size the user types: rows outside, columns inside."""

# the data
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

# the work
M = [[0 for c in range(cols)] for r in range(rows)]

# the answer
print(M)
