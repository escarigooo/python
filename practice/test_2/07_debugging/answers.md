# Debugging answers

Read only after writing the issue, faulty line, corrected line, and expected output
on paper.

## 1 - `01_while_update.py`

The update is calculated but discarded:

```python
n = n - 1
```

## 2 - `02_break_position.py`

`break` runs before the condition. It belongs inside the matching `if`, after `print`:

```python
for value in values:
    if value > 50:
        print(value)
        break
```

## 3 - `03_counter_scope.py`

Reset the counter once per row:

```python
for row in matrix:
    even_count = 0
    for value in row:
        if value % 2 == 0:
            even_count = even_count + 1
    print(even_count)
```

## 4 - `04_rows_and_columns.py`

Reset the accumulator per row and use row before column:

```python
for row in range(len(matrix)):
    total = 0
    for column in range(len(matrix[row])):
        total = total + matrix[row][column]
    print(total)
```

## 5 - `05_comprehension_pipeline.py`

```python
names = text.split(";")
long_names = [name.upper() for name in names if len(name) > 3]
count = 0
for name in long_names:
    count = count + 1
```

## 6 - `06_list_aliasing.py`

`copy_values = values` creates an alias. A slice creates a new outer list:

```python
copy_values = values[:]
```
