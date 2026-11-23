# Functions

Complete the files in `official/` in order. Trace every call on paper, tracking what
arguments are passed in, what is printed, and what value is returned.

## Key patterns

Defining and calling a function:

```python
def add(a, b):
    result = a + b
    return result

z = add(5, 3)
```

Positional and keyword arguments:

```python
show_pair(3, 5)          # positional: a=3, b=5
show_pair(b=5, a=3)      # keyword: a=3, b=5
```

Important rules:

- `def` creates the function without running its body; parentheses `()` run it.
- `return` immediately stops the function and hands back a value to the caller.
- `print` only displays output; a function without `return` hands back `None`.
- Reassigning a parameter (`x = x + 4`) inside a function does not change an
  immutable variable outside it, whereas mutating a passed list or matrix does.

High-risk mistakes: printing instead of returning, forgetting to capture a returned
value, resetting a counter inside a loop, confusing positional argument order, and
mutating a matrix in place when a new matrix was required.

Check your work against `../solutions/week12_answer_key.md` only after two honest
attempts.
