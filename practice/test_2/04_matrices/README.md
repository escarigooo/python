# Matrices and conditional expressions

Complete the files in `official/` in order. Predict every output on paper before
running the program, paying close attention to whether two names share the same list
or row.

## Key patterns

Independent matrix of zeros (rows outside, columns inside):

```python
M = [[0 for c in range(cols)] for r in range(rows)]
```

Copying a matrix row by row (changes through `B` leave `A` unchanged):

```python
B = [row[:] for row in A]
```

Conditional expression (one value, in one line):

```python
absolute = n if n >= 0 else -n
absolutes = [n if n >= 0 else -n for n in nums]
```

Mutation versus rebinding after `b = a`:

- Mutates the shared list: `b[0] = 5`, `b.append(40)`, `b += [40]`.
- Rebinds `b` to a new list: `b = [7]`, `b = a[:]`, `b = b + [40]`.

High-risk mistakes: building a matrix with `[row, row, row]` (shared rows), using
`B = A[:]` on a 2D list (outer list is copied, inner rows are still shared), swapping
row and column ranges, and putting a filter `if` in the wrong position compared to a
conditional expression `a if cond else b`.

Official code answers are in `../solutions/week11_official/`. Exercises 11 and 12 are
bridge exercises that lead directly into Week 12 (`05_functions`).
