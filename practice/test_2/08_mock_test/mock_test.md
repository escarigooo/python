# Mock Coding Test 2 - Weeks 8-10

## Group 1 - Trace and choose (6 points)

### 1

What prints?

```python
n = 7
while n > 1:
    print(n, end=" ")
    n = n - 2
print(n)
```

A. `7 5 3 1`  B. `7 5 3`  C. `7 6 5 4 3 2 1`  D. infinite loop

### 2

What prints?

```python
for value in [4, 9, 12, 20]:
    if value % 3 == 0:
        print(value)
        break
```

A. `4`  B. `9`  C. `9 12`  D. `12`

### 3

How many times does `print()` run?

```python
for i in range(3):
    for j in range(i + 1):
        print(i, j)
```

A. 3  B. 5  C. 6  D. 9

### 4

What is `matrix[1][2]`?

```python
matrix = [[8, 3, 1], [4, 9, 7]]
```

A. `1`  B. `4`  C. `7`  D. `9`

### 5

What prints?

```python
values = [n * 2 for n in range(1, 5) if n % 2 == 0]
print(values)
```

A. `[2, 4, 6, 8]`  B. `[4, 8]`  C. `[2, 4]`  D. `[1, 2, 3, 4]`

### 6

What prints?

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

A. `[1, 2]`  B. `[1, 2, 3]`  C. `None`  D. error

## Group 2 - Find and fix (4 points)

For each program, state the issue and rewrite every faulty line.

### 7

The program should ask until the user enters a value from 1 through 5.

```python
number = input("Number: ")
while number < 1 or number > 5:
    number = input("Number: ")
print("accepted")
```

### 8

The program should print each matrix row's total: `3` and then `7`.

```python
matrix = [[1, 2], [3, 4]]
total = 0
for row in matrix:
    for value in row:
        total = value
    print(total)
```

## Group 3 - Fill the blanks (2 points)

Complete a list of lowercase positive integers from comma-separated input:

```python
text = "3,-1,8,0,5"
numbers = [<A> for part in <B> if <C>]
print(numbers)
```

Expected: `[3, 8, 5]`

## Group 4 - Open program (8 points)

Given:

```python
temperatures = [
    [12, -2, 18],
    [7, 21, 5],
    [-1, 9, 14],
]
```

Write a program that:

1. prints every value with its row and column;
2. prints the sum of each row without using `sum()`;
3. uses a separate nested search to print the first negative value and its position,
   then stops that search;
4. builds, with one double list comprehension, a flat list containing only the
   non-negative values;
5. prints the largest row sum without using `max()`.
