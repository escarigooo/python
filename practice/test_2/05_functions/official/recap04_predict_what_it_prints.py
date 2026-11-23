"""Read the program below and write exactly the line it prints — every bracket in its place.
On paper, before any run.
Then run it and compare.
"""

def row_of(M, i):
    return M[i]

def copy_of(M, i):
    return M[i][:]

grid = [[1, 2], [3, 4], [5, 6]]
a = row_of(grid, i=0)
b = copy_of(i=1, M=grid)
c = row_of(grid, len(grid) - 1)[::-1]
a[0] = b[0] + c[0]
b[1] = a[1] * 10
c.append(a[0])
print(grid, a, b, c)
