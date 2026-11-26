# Functions

Complete the files in `official/` in order. Trace every call on paper, tracking what
arguments are passed in, what is printed, and what value is returned.

Also work through the [Week 12 practical handout](../../../materials/handouts/week-12-lists-and-functions.pdf).
Its eight exercises mix list input, validation, string slicing, matrices, and the first
function definitions. In particular, practise returning a value or list to the caller;
do not replace a required `return` with `print`.

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

## Answers

Check your work against [`answers.md`](answers.md) right here in this folder only after
two honest attempts.

## Try on LeetCode after finishing

- [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [66. Plus One](https://leetcode.com/problems/plus-one/)
- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

See [`../LEETCODE_MAP.md`](../LEETCODE_MAP.md) for the full list and starter-code tips.
