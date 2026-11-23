"""Write the loop that prints the first column, one value per line — exactly as the output below shows. Start from the matrix in the panel."""

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(M)):
    print(M[i][0])  # 1, then 4, then 7 - one value per line

# the same column, walking the rows themselves:
# for row in M:
#     print(row[0])
