# Nested loops and matrices

Complete the files in `official/` in order. Exercises 7, 11, 12, 13, 14, and all
recaps are the strongest exam preparation.

Execution rule:

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

The inner loop finishes completely before the outer loop advances. The body runs
`2 * 3 = 6` times.

Matrix patterns:

```python
matrix[row][column]

for row in matrix:
    for value in row:
        print(value)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
```

Reset a per-row counter inside the outer loop and before the inner loop.
