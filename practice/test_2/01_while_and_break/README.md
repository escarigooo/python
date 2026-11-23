# While and break

Complete the files in `official/` in their numbered order.

Core pattern:

```python
state = initial_value

while condition_using(state):
    # work
    state = updated_value
```

Before running a `while`, identify:

- the initial state;
- the condition;
- the update;
- the first state that makes the condition false.

Use `break` when the loop must stop immediately:

```python
for value in values:
    if value < 0:
        print(value)
        break
```

High-risk mistakes: uninitialised state, missing update, comparing a string with an
integer, updating outside the loop, and placing `break` before required work.

## Answers

Official code answers are right here in [`answers/`](answers/).

## Try on LeetCode after finishing

- [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)
- [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)
- [258. Add Digits](https://leetcode.com/problems/add-digits/)
- [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

See [`../LEETCODE_MAP.md`](../LEETCODE_MAP.md) for the full list and starter-code tips.
