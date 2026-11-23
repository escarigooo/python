"""Print the number of even values in each row. Expected: 2, then 1, then 3.
The program prints cumulative counts. Explain where the counter must reset."""

matrix = [[2, 5, 8], [1, 4, 7], [6, 10, 12]]
even_count = 0
for row in matrix:
    for value in row:
        if value % 2 == 0:
            even_count = even_count + 1
    print(even_count)
