"""Print each row's sum: 6, 15, and 24. The program prints column sums instead.
Identify the incorrect indexing and any accumulator-placement problem."""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        total = total + matrix[column][row]
    print(total)
