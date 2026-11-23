"""Write the loop that prints the diagonal of the 3-by-3 matrix,
one value per line — exactly as the output below shows.
Start from the matrix in the panel. One loop is enough."""

M = [[2, 0, 0], [0, 5, 0], [0, 0, 9]]
for i in range(len(M)):
    print(M[i][i])  # 2, then 5, then 9 - one value per line
