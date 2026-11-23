"""A matrix made of the same row three times: one element is set, three rows change."""

# the data
row = [0, 0, 0]
M = [row, row, row]

# the work
M[0][0] = 1

# the answer
print(M)
