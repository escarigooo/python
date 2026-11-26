# 30-minute diagnostic

**Time: 30 minutes | Total: 20 points**

Do this on paper. Do not run the code or read `solutions.md` until the timer ends.

## Part 1 - Trace and choose (6 points, 6 minutes)

Choose one answer for each question. Each question is worth 1 point.

### 1. `while` and `break`

What does this print?

```python
n = 1
while n < 10:
    n = n * 2
    if n == 8:
        break
print(n)
```

A. `4`

B. `8`

C. `10`

D. It never stops

### 2. Nested loops

What is the final value of `count`?

```python
count = 0
for row in range(1, 4):
    for column in range(row):
        count = count + 1
```

A. `3`

B. `4`

C. `6`

D. `9`

### 3. Double list comprehension

What is the value of `pairs`?

```python
pairs = [(a, b) for a in [1, 2] for b in [1, 2] if a != b]
```

A. `[(1, 1), (1, 2), (2, 1), (2, 2)]`

B. `[(1, 2), (2, 1)]`

C. `[(1, 2)]`

D. `[(2, 1), (1, 2)]`

### 4. Copying a matrix

Which line makes a new outer list and a new copy of each row, so changing one cell
in `copy` does not change `matrix`?

A. `copy = matrix`

B. `copy = matrix[:]`

C. `copy = [row[:] for row in matrix]`

D. `copy = [row for row in matrix]`

### 5. Parameter scope

What does this print?

```python
def bump(number):
    number = number + 4
    return number

x = 3
print(bump(x), x)
```

A. `7 7`

B. `7 3`

C. `3 7`

D. `None 3`

### 6. Mutation and return

What does this print?

```python
def add_value(items, value):
    items.append(value)
    value = value + 1
    return value

numbers = [2]
print(add_value(numbers, 5), numbers)
```

A. `6 [2]`

B. `5 [2, 5]`

C. `6 [2, 5]`

D. `None [2, 5]`

## Part 2 - Find and fix (4 points, 6 minutes)

For each question, state the issue briefly and rewrite the faulty line or lines.
Each question is worth 2 points.

### 7. Read an integer and repeat until it is valid

This should keep asking until the user enters an integer from 1 through 5.

```python
number = input("Number: ")
while number < 1 or number > 5:
    number = input("Number: ")
print("accepted")
```

### 8. Count every matching value

This function should return how many values are greater than `limit`.

```python
def count_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            count = count + 1
            return count
```

## Part 3 - Fill the blanks (3 points, 3 minutes)

Complete the function so it returns the indexes of values that are at least `limit`.
Each blank is worth 0.75 points.

```python
def indexes_at_least(values, limit):
    indexes = []
    for i in range(<A>):
        if values[i] >= <B>:
            indexes.append(<C>)
    return <D>
```

For `indexes_at_least([12, 5, 17, 10], 10)`, the result should be `[0, 2, 3]`.

## Part 4 - Write a small program (7 points, 15 minutes)

Given this matrix of scores:

```python
scores = [
    [12, 8, 15],
    [10, 17, 9],
    [20, 6, 11],
]
```

Write a program that does all of the following:

1. Define `row_totals(matrix)`. Use nested loops to return a list containing the
   total of each row. Do not use `sum()`. **(3 points)**
2. Define `passing_scores(matrix, limit)`. Use one double list comprehension to
   return a flat list of all scores greater than or equal to `limit`. **(2 points)**
3. Call both functions and print their results. Use a keyword argument when calling
   `passing_scores`. **(1 point)**
4. Find and print the largest row total without using `max()`. **(1 point)**

Your output should include:

```text
[35, 36, 37]
[12, 15, 10, 17, 20, 11]
Largest row total: 37
```
