# Mock test solutions

Do not read before completing the timed attempt.

## Group 1

1. A - the states printed are 7, 5, 3, and then the final 1.
2. B - 9 is the first value divisible by 3, then `break` exits.
3. C - the inner loop runs 1 + 2 + 3 = 6 times.
4. C - row index 1 is `[4, 9, 7]`; column index 2 is `7`.
5. B - only 2 and 4 pass the filter, then each is doubled.
6. B - `a` and `b` refer to the same mutable list.

## Group 2

### 7

`input()` returns text, so numeric comparison requires conversion in both input lines:

```python
number = int(input("Number: "))
while number < 1 or number > 5:
    number = int(input("Number: "))
```

### 8

The accumulator must reset for each row and must add rather than replace:

```python
for row in matrix:
    total = 0
    for value in row:
        total = total + value
    print(total)
```

## Group 3

```python
numbers = [int(part) for part in text.split(",") if int(part) > 0]
```

- A: `int(part)`
- B: `text.split(",")`
- C: `int(part) > 0`

## Group 4

```python
row_sums = []

for row_index in range(len(temperatures)):
    row_total = 0

    for column_index in range(len(temperatures[row_index])):
        value = temperatures[row_index][column_index]
        print(value, row_index, column_index)
        row_total = row_total + value

    row_sums.append(row_total)
    print("row total:", row_total)

found_negative = False
for row_index in range(len(temperatures)):
    for column_index in range(len(temperatures[row_index])):
        value = temperatures[row_index][column_index]
        if value < 0:
            print("first negative:", value, row_index, column_index)
            found_negative = True
            break
    if found_negative:
        break

non_negative = [
    value
    for row in temperatures
    for value in row
    if value >= 0
]
print(non_negative)

largest = row_sums[0]
for row_total in row_sums:
    if row_total > largest:
        largest = row_total
print("largest row sum:", largest)
```

The first pair of loops produces the complete report. The separate search uses `break`
for the inner loop and the flag to leave the outer loop after the first negative.
