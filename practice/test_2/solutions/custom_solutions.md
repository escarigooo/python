# Custom practice solutions

Read only after two complete attempts. Different correct solutions are valid when
they obey the exercise restrictions.

## Complex 1 - Password gate

```python
attempts = 0

while True:
    password = input("Password: ")
    attempts = attempts + 1
    uppercase_count = 0
    digit_count = 0

    for character in password:
        if character.isupper():
            uppercase_count = uppercase_count + 1
        if character.isdigit():
            digit_count = digit_count + 1

    if uppercase_count >= 2 and digit_count >= 1:
        break

    if uppercase_count < 2:
        print("Need at least two uppercase letters.")
    if digit_count < 1:
        print("Need at least one digit.")

print(f"Accepted after {attempts} attempts.")
```

## Complex 2 - Matrix row report

```python
largest_row = 0
largest_total = 0

for row_index in range(len(matrix)):
    total = 0
    even_count = 0

    for value in matrix[row_index]:
        total = total + value
        if value % 2 == 0:
            even_count = even_count + 1

    print(f"row {row_index}: total={total}, evens={even_count}")

    if row_index == 0 or total > largest_total:
        largest_total = total
        largest_row = row_index

print(f"largest row: {largest_row}")
```

## Complex 3 - First free seat

```python
found = False

for row in range(len(seats)):
    for column in range(len(seats[row])):
        if seats[row][column] == 0:
            print(f"first free seat: row {row}, column {column}")
            found = True
            break
    if found:
        break

if not found:
    print("full")
```

## Complex 4 - Clean measurements

```python
measurements = [
    int(part.strip())
    for part in text.split(",")
    if 0 <= int(part.strip()) <= 100
]
print(measurements)
```

## Complex 5 - Pairings

```python
pairings = [
    first + " " + last
    for first in first_names
    for last in last_names
    if first[0].lower() != last[0].lower()
]
print(pairings)
```

## Complex 6 - Integrated results

```python
results = []

while True:
    line = input("Grades, or done: ").strip()
    if line.lower() == "done":
        break

    parts = line.split(",")
    row = []
    valid = len(parts) > 0

    for part in parts:
        cleaned = part.strip()
        if not cleaned.isdigit():
            valid = False
        else:
            grade = int(cleaned)
            if grade < 0 or grade > 20:
                valid = False
            else:
                row.append(grade)

    if valid:
        results.append(row)
    else:
        print("Invalid row.")

total_grade_count = 0
for row_index in range(len(results)):
    row_total = 0
    for grade in results[row_index]:
        row_total = row_total + grade
        total_grade_count = total_grade_count + 1
    print(f"row {row_index} average: {row_total / len(results[row_index])}")

passing = [
    grade
    for row in results
    for grade in row
    if grade >= 10
]

print(passing)
print(f"total grades: {total_grade_count}")
print(f"passing grades: {len(passing)}")
```

## Debugging answers

### 1

The update is calculated but discarded:

```python
n = n - 1
```

### 2

`break` runs before the condition. It belongs inside the matching `if`, after print:

```python
for value in values:
    if value > 50:
        print(value)
        break
```

### 3

Reset the counter once per row:

```python
for row in matrix:
    even_count = 0
    for value in row:
        if value % 2 == 0:
            even_count = even_count + 1
    print(even_count)
```

### 4

Reset the accumulator per row and use row before column:

```python
for row in range(len(matrix)):
    total = 0
    for column in range(len(matrix[row])):
        total = total + matrix[row][column]
    print(total)
```

### 5

```python
names = text.split(";")
long_names = [name.upper() for name in names if len(name) > 3]
count = 0
for name in long_names:
    count = count + 1
```

### 6

`copy_values = values` creates an alias. A slice creates a new outer list:

```python
copy_values = values[:]
```
