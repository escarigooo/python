# LeetCode Practice Map (Computation I — Weeks 1–12)

Every LeetCode problem below can be solved using **only the Python syntax taught through
Week 12** (variables, strings, lists, `if`, `for`, `while`, `break`, nested loops,
matrices, list comprehensions, conditional expressions, and functions). No dictionaries,
sets, classes, or recursion are required.

## Quick tip: How to read LeetCode's starter code

LeetCode wraps your function inside `class Solution:` and adds `self` as the first
parameter:

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Write your normal function body here, indented inside def!
        # Ignore `class Solution:` and `self` — just use `num` and `return` your answer.
        steps = 0
        while num > 0:
            num = num // 2 if num % 2 == 0 else num - 1
            steps += 1
        return steps
```

- Always **`return`** the answer (never `print` it).
- You can ignore the type hints (`: int`, `-> int`, `List[int]`) — they just tell you
  what type the parameter and return value are.

---

## Stage 1 — `while` and `break` (`01_while_and_break/`)

| LeetCode Problem | Difficulty | Course parallel | Key concepts |
| --- | --- | --- | --- |
| [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | Week 8 `ex01`–`ex02` & Week 12 `recap05` | `while n > 0`, `% 2`, `// 2`, step counter |
| [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | Easy | Week 8 accumulators | `while n > 0`, `% 10`, `// 10` |
| [258. Add Digits](https://leetcode.com/problems/add-digits/) | Easy | Week 8 nested `while` | Repeat summing digits `while num >= 10` |
| [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | Strings + `while` | `str(x) == str(x)[::-1]` or digit-by-digit `while` |

## Stage 2 — Nested loops & matrices (`02_nested_loops_and_matrices/`)

| LeetCode Problem | Difficulty | Course parallel | Key concepts |
| --- | --- | --- | --- |
| [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | Week 9 `recap03` & `06_complex_practice/02` | Per-row sum in a matrix + tracking the maximum |
| [1572. Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | Easy | Week 9 `ex14_the_trace` & Week 11 `ex06` | Main diagonal `mat[i][i]` + secondary diagonal `mat[i][n - 1 - i]` |
| [1351. Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | Easy | Week 9 `ex07_evens_in_each_row` | Nested loop counting cells `< 0` |
| [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Easy | Week 9 nested loops | `for i in range(len(nums)):` / `for j in range(i + 1, len(nums)):` |

## Stage 3 — List comprehensions (`03_list_comprehensions/`)

| LeetCode Problem | Difficulty | Course parallel | Key concepts |
| --- | --- | --- | --- |
| [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | Week 11 Practical Ex 6 | `nums + nums` or comprehension |
| [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/) | Easy | Week 10 `ex01`–`ex03` | `[nums[nums[i]] for i in range(len(nums))]` |
| [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | Easy | Week 10 `ex09` | Find max, then `[c + extraCandies >= best for c in candies]` |
| [2114. Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) | Easy | Week 10 `ex04`–`ex05` | `split()` + `len()` in a comprehension |
| [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | Week 12 `recap03` (`running_max`) | Building a running-total list |

## Stage 4 — Matrices & conditional expressions (`04_matrices/`)

| LeetCode Problem | Difficulty | Course parallel | Key concepts |
| --- | --- | --- | --- |
| [867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | Easy | **Week 12 `recap06` (`flip`)** | `[[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]` |
| [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/) | Easy | Week 11 `ex09` & `ex10` | Reverse row `row[::-1]` + conditional expression `1 if v == 0 else 0` |
| [2022. Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | Easy | Week 11 `ex08` & Practical Ex 2 | Building a new `m × n` matrix from slices |
| [2500. Delete Greatest Value in Each Row](https://leetcode.com/problems/delete-greatest-value-in-each-row/) | Easy | Week 11 matrix copying + columns | Row operations + column-by-column max |

## Stage 5 — Functions & combined mastery (`05_functions/` & `06_complex_practice/`)

| LeetCode Problem | Difficulty | Course parallel | Key concepts |
| --- | --- | --- | --- |
| [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | Conditionals + `for` + `return` | `if/elif/else`, `%`, building and returning a list |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Nested loops + `return` | Brute-force `for i` / `for j` returning `[i, j]` |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Week 12 `10_your_turn_no_digits_upper` | Filtering characters (`.isalnum()`, `.lower()`) + `[::-1]` |
| [66. Plus One](https://leetcode.com/problems/plus-one/) | Easy | Lists + reverse traversal + `return` | Carrying digits from right to left |
| [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | Nested loops + `break` + `return` | Comparing characters across a list of strings |
| [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Week 11 in-place mutation | Modifying a list in place without returning a new one |

---

## Recommended workflow

1. Finish a stage's exercises in `official/` and check against its `answers/` folder.
2. Pick **2 LeetCode problems** from that stage above and solve them on
   [leetcode.com](https://leetcode.com) without looking at hints.
3. If you solve them cleanly, you know you can handle exam variations you've never seen before!
