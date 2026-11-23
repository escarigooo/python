"""A matrix copied row by row: a change through B leaves A whole."""

# the data
A = [[1, 2], [3, 4]]

# the work
B = [row[:] for row in A]
B[0][0] = 9

# the answer
print(A)
print(B)
