"""Walks the matrix by index:
i counts the rows,
j the columns,
and the body reads m[i][j].
"""

# the matrix
m = [[7, 2, 9], [4, 1, 5]]
# the walk
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
    print()
