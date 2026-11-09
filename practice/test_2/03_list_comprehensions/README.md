# List comprehensions

Complete the files in `official/` in order. Always write the equivalent ordinary
loop beside a difficult comprehension.

One loop:

```python
result = [expression for item in sequence]
```

Filter:

```python
result = [expression for item in sequence if condition]
```

Two loops:

```python
result = [expression for outer in sequence_1 for inner in sequence_2]
```

Read two loops from left to right: the first `for` is the outer loop and the second
is the inner loop. The expression at the beginning is the value appended each time.

High-risk mistakes: wrong separator in `split()`, forgetting conversion, missing
method parentheses, putting the filter before the `for`, and reversing loop order.
