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

## Answers

Official code answers are right here in [`answers/`](answers/).

## Try on LeetCode after finishing

- [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)
- [1572. Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/)
- [1351. Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
- [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

See [`../LEETCODE_MAP.md`](../LEETCODE_MAP.md) for the full list and starter-code tips.
