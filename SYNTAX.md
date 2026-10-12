# Python syntax reference

Try to write syntax from memory before opening this file.

## Values, variables, and output

```python
name = "Ana"
age = 20
average = 16.5
is_student = True

print(name)
print("Age:", age)
print(f"{name} has an average of {average}")
```

Common types are `int`, `float`, `str`, `bool`, and `list`.

## Input and conversion

```python
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))

int("42")
float("3.5")
str(42)
type(age)
```

`input()` always returns a string. Convert it before doing numerical calculations.

## Operators

```python
a + b       # addition
a - b       # subtraction
a * b       # multiplication
a / b       # division
a // b      # floor division
a % b       # remainder
a ** b      # exponentiation

a == b      # equal
a != b      # not equal
a < b
a <= b
a > b
a >= b

condition_a and condition_b
condition_a or condition_b
not condition_a
```

Use `=` to assign a value and `==` to compare two values.

## Strings

```python
text = "Python"

text[0]                 # first character
text[-1]                # last character
text[1:4]               # positions 1, 2, and 3
len(text)
text.lower()
text.upper()
text.replace("P", "J")
"Py" in text
```

Indexes begin at `0`. The ending position of a slice is excluded.

## Conditions

```python
if grade >= 18:
    print("Excellent")
elif grade >= 10:
    print("Passed")
else:
    print("Failed")
```

The colon and indentation are part of Python's syntax.

## Loops

```python
for number in range(1, 6):
    print(number)

for letter in "Python":
    print(letter)

count = 0
while count < 5:
    print(count)
    count += 1
```

Use `for` when iterating over a sequence. Use `while` when repetition depends on a
condition.

## Lists

```python
grades = [14, 17, 19]

grades[0]
grades[-1]
grades.append(16)
grades.pop()
len(grades)
17 in grades

for grade in grades:
    print(grade)
```

## Functions

```python
def calculate_average(first, second):
    total = first + second
    return total / 2


result = calculate_average(14, 18)
```

Parameters are written inside the parentheses. `return` sends a result back to the
caller; `print` only displays something.

## Matrices as nested lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

value = matrix[1][2]

for row in matrix:
    for value in row:
        print(value)
```

## Useful error meanings

- `SyntaxError`: Python cannot understand the structure of the code.
- `NameError`: a name has not been defined, or it is misspelled.
- `TypeError`: an operation received an incompatible type.
- `ValueError`: the type is acceptable, but the value is not.
- `IndexError`: a string or list position does not exist.
- `IndentationError`: the indentation does not form a valid block.
