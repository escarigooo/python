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

## Answers

Official code answers and the summary key are right here in [`answers/`](answers/).

## Try on LeetCode after finishing

- [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)
- [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/)
- [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
- [2114. Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)
- [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

See [`../LEETCODE_MAP.md`](../LEETCODE_MAP.md) for the full list and starter-code tips.
