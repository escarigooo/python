# Hardest Practical Class Problems — Review & Solved Walkthroughs

This guide collects the most complex exercises from the official practical classes and
recaps (Weeks 8–12) in one place, followed by fully resolved, line-by-line walkthroughs
of the toughest ones.

## Index of the hardest practical problems

| Week | Source | Exercise | Core concepts tested |
| --- | --- | --- | --- |
| 08 | `01_while_and_break/official/` | `ex09_a_program_that_chats.py`, `recap03` | Sentinel `while` loop, `break`, accumulator updates |
| 09 | `materials/handouts/week-09-exercises-i.pdf` | **Exercise 8** (Valid grade 0–20) | `while` validation with `.isdigit()` + short-circuit `or` |
| 09 | `02_nested_loops_and_matrices/official/` | `ex11_check_every_row.py`, `ex12_print_the_columns.py`, `ex14_the_trace.py` | Nested loops, per-row flags, column-major indexing, diagonal trace |
| 10 | `materials/handouts/week-10-list-comprehensions.pdf` | **Exercise 6** (THREENGO!) | Chaining 3 comprehensions (input, random, membership filter) |
| 10 | `materials/handouts/week-10-list-comprehensions.pdf` | **Exercise 9** (Chessboard black squares) | Double comprehension, index mapping (`let - 1`), parity filter (`% 2`) |
| 11 | `materials/handouts/week-11-matrices.pdf` | **Exercise 4** (Matrix addition `A + B`) | Nested comprehensions for 2D input and element-wise `A[i][j] + B[i][j]` |
| 11 | `materials/handouts/week-11-matrices.pdf` | **Exercise 6** (Interactive list/matrix menu) | Input comprehension, `if/elif/else`, building a 3-row matrix, concatenation |
| 12 | `05_functions/official/` | **Recap 1**, **Recap 4**, **Recap 6 (`flip`)** | Functions returning matrices, aliasing vs. copying (`[:]`), matrix transpose |

---

## Fully Resolved Walkthroughs

### 1. Hardest Practical Handout Problem — Week 11, Exercise 4 (Matrix Addition)

**Prompt:** Ask the user for the number of rows and columns, let them insert two
matrices `A` and `B` of that size, and compute a new matrix where every element is
`A[i][j] + B[i][j]`.

#### Official solution

```python
row = int(input("Number of rows: "))
column = int(input("Number of columns: "))

A = [[int(input("Insert an integer: ")) for j in range(column)] for i in range(row)]
B = [[int(input("Insert an integer: ")) for j in range(column)] for i in range(row)]

matrix_sum = [[A[i][j] + B[i][j] for j in range(column)] for i in range(row)]

print(f"A: {A}")
print(f"B: {B}")
print(f"Sum: {matrix_sum}")
```

#### Line-by-line breakdown

1. **Read dimensions:** `row` and `column` are converted with `int()` because `range()`
   requires integers.
2. **Build `A` and `B` with nested comprehensions:**
   - Read from the **outside in**:
     - Outer loop `for i in range(row)` runs once per row (creating `row` inner lists).
     - Inner loop `[int(input(...)) for j in range(column)]` runs `column` times to
       fill a single row.
   - Because the inner list is created fresh on every outer iteration, every row is an
     **independent** list (no row-aliasing bug).
3. **Add element by element:**
   - `A[i][j] + B[i][j]` accesses the exact same row `i` and column `j` in both matrices.
   - Equivalent ordinary nested loop (always write this on paper if the comprehension
     feels dense):

```python
matrix_sum = []
for i in range(row):
    current_row = []
    for j in range(column):
        current_row.append(A[i][j] + B[i][j])
    matrix_sum.append(current_row)
```

4. **Dry run** with `row = 2`, `column = 2`, `A = [[1, 2], [3, 4]]`, `B = [[5, 6], [7, 8]]`:
   - `i = 0`: `j = 0` → `1 + 5 = 6`; `j = 1` → `2 + 6 = 8` → row `[6, 8]`
   - `i = 1`: `j = 0` → `3 + 7 = 10`; `j = 1` → `4 + 8 = 12` → row `[10, 12]`
   - Result: `[[6, 8], [10, 12]]`.

---

### 2. Hardest Comprehension Problem — Week 10, Exercise 9 (Chessboard Black Squares)

**Prompt:** On an 8×8 chessboard (columns `A`–`H` numbered `1`–`8`, rows `1`–`8`), use
a list comprehension to produce only the black squares (where column and row are both
odd or both even).

#### Official solution

```python
letters = "ABCDEFGH"
numbers = range(1, 9)
chessboard = [
    str(letters[let - 1]) + str(numb)
    for let in numbers
    for numb in numbers
    if let % 2 == numb % 2
]
print(chessboard)
```

#### Why this is tricky (and how to read it)

- **Why `let` goes from `1` to `8` instead of iterating over `letters` directly:**
  You need the column's **number** (`1` for `A`, `2` for `B`, …) to check whether it is
  odd or even (`let % 2`). Then `letters[let - 1]` converts `1..8` back into 0-based
  string indexes `0..7` (`'A'..'H'`).
- **Why `let % 2 == numb % 2` works:**
  - Odd % 2 is `1`; Even % 2 is `0`.
  - They are equal if and only if both are odd (`1 == 1`) or both are even (`0 == 0`).
- **Loop order:** Read left to right — `let` is the outer loop (`A` first, then `B`, …),
  `numb` is the inner loop (`1, 3, 5, 7` for `A`; `2, 4, 6, 8` for `B`).

---

### 3. Hardest Validation Pattern — Week 9, Exercise 8 (Safe Grade Input)

**Prompt:** Keep asking until the user enters a whole number between `0` and `20`
(without crashing if they type `"abc"`).

```python
grade = input("Gimme grade: ")

while not grade.isdigit() or not 0 <= int(grade) <= 20:
    grade = input("Dude... I said your grade... Try again: ")

grade = int(grade)
if grade > 17:
    print("Yay!!")
else:
    print(":)")
```

**Exam trap:** The order in `not grade.isdigit() or not 0 <= int(grade) <= 20` matters!
When `grade` is `"abc"`, `not grade.isdigit()` is `True`, so Python **short-circuits**
the `or` and never runs `int("abc")` (which would raise `ValueError`). Reversing the
two sides would crash.

---

### 4. Hardest Exam-Style Synthesis — Week 12, Recap 6 (`flip` — Matrix Transpose)

**Prompt:** Write `flip(M)` in a single `return` line so that row `j` of the result
holds column `j` of `M` (turning a `2 × 3` matrix into a `3 × 2` matrix):

```python
def flip(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]

print(flip([[1, 2, 3], [4, 5, 6]]))
# Output: [[1, 4], [2, 5], [3, 6]]
```

**Why this is the ultimate Coding Test 2 check:**
- Outer loop (`for j in range(len(M[0]))`) iterates over the **columns** of `M` (`0, 1, 2`) — creating **3 output rows**.
- Inner loop (`for i in range(len(M))`) iterates over the **rows** of `M` (`0, 1`) — picking `M[0][j]` and `M[1][j]` for each output row.
- If you accidentally swap `len(M)` and `len(M[0])`, or swap `M[i][j]` to `M[j][i]`, you either lose a column or hit `IndexError`.
