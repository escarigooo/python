"""The same matrix, each position holding a slice of the row: one row changes."""

# the data
row = [0, 0, 0]
M = [row[:], row[:], row[:]]

# the work
M[0][0] = 1

# the answer
print(M)
