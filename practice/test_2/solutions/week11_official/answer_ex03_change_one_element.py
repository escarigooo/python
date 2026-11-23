"""Write the two lines that set the middle element to 0, then print the whole matrix —
exactly as the output below shows.
Start from the matrix given in the panel and change it in place: this lecture’s mutation, by position."""

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M[1][1] = 0
print(M)  # [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
