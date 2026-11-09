"""Walks the matrix by element:
the outer loop takes the rows,
the inner one their values.
"""

# the matrix
m = [[7, 2, 9], [4, 1, 5]]
# the walk
for row in m:
    for value in row:
        print(value, end=" ")
    print()
