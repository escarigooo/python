# Week 12 answer key

Attempt every official file in `05_functions/official/` before reading this page.

## Exercises

1.

```python
def welcome():
    print("Welcome to Computation I")

welcome()
```

2.

```text
A
B
C
B
```

3.

```python
def double(n):
    return n * 2
```

4.

```text
Ana-7
Ana-7
7-Ana
```

5. `bigger` uses `print` instead of `return` (so the calls return `None`), and its
`else` branch handles both `b > a` and `a == b`. Fix:

```python
def bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    return None
```

6.

```python
def count_above(values, limit):
    count = 0
    for v in values:
        if v > limit:
            count = count + 1
    return count
```

7. `80 60.0` (reassigning `price` inside `discount` does not change the outer `price`,
and the second call's return value is not saved).

8.

```python
def scale(M, factor):
    return [[v * factor for v in row] for row in M]
```

9. Three faulty lines:
   - `count = 0` is inside the `for` loop, resetting `count` on every iteration; move it
     before the `for` loop.
   - `if g > limit:` excludes grades equal to `limit`; change it to `if g >= limit:`.
   - `print(total / count)` prints instead of returning (leaving `result` as `None`);
     change it to `return total / count`.

```python
def average_above(grades, limit):
    total = 0
    count = 0
    for g in grades:
        if g >= limit:
            total = total + g
            count = count + 1
    return total / count
```

10. `<A>` is `-1`, `<B>` is `values[i] > limit`, and `<C>` is `break`.

11.

```python
print(area(5) - area(2))
```

## Recaps

1. `3 |64||`

2.

```text
area 5 2
area 3 10
show 30
area 5 5
area 9 9
10 None [25, 81]
```

3. **D** (`<X> = L[0]`, `<Y> = v if v > best else best`).
   - A fails on all-negative lists (starts `best` at `0`, returning `[0, 0, 0]`).
   - B keeps the smaller value instead of the larger (running minimum).
   - C sets `best` to a boolean (`True`/`False`) instead of a number.
   - E raises a `TypeError` comparing an `int` with `[]`.
   - F always compares against `L[0]` instead of the running `best` (for `[3, 1, 4, 2, 5]` it gives `[3, 3, 4, 3, 5]`).

4. `[[9, 2], [3, 4], [5, 6]] [9, 2] [3, 20] [6, 5, 9]`

5. `6 8 3`

6. **E** (`return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]`).
   - A returns a copy of `M` unchanged (`[[1, 2, 3], [4, 5, 6]]`).
   - B returns a flat list (`[1, 4, 2, 5, 3, 6]`).
   - C uses `len(M)` for both ranges, dropping the last column (`[[1, 4], [2, 5]]`).
   - D swaps `i` and `j` in `M[j][i]`, raising `IndexError` when `j == 2`.
   - F reverses the row order (`[[4, 5, 6], [1, 2, 3]]`).
   - G reverses each row before transposing (`[[3, 6], [2, 5], [1, 4]]`).
