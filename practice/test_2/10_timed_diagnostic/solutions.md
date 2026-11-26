# Solutions - open only after the 30-minute attempt

## Part 1 - Trace and choose

1. **B - `8`.** The values assigned to `n` are 2, 4, and 8. At 8, `break` exits
   the loop before another update.
2. **C - `6`.** The inner loop runs 1 time for row 1, 2 for row 2, and 3 for row 3:
   `1 + 2 + 3 = 6`.
3. **B - `[(1, 2), (2, 1)]`.** The outer value `a` changes more slowly; the inner
   value `b` visits 1 then 2 for each `a`. Equal pairs are filtered out.
4. **C - `copy = [row[:] for row in matrix]`.** The comprehension copies every row
   as well as creating a new outer list. `matrix[:]` alone is only a shallow copy.
5. **B - `7 3`.** The function reassigns its local parameter. The outer `x` stays 3.
6. **C - `6 [2, 5]`.** `append()` mutates the list passed in. Reassigning the local
   integer parameter `value` does not change the caller's variable; the returned
   value is 6.

## Part 2 - Find and fix

### 7

`input()` returns a string, so both input values must be converted to integers before
the numeric comparisons:

```python
number = int(input("Number: "))
while number < 1 or number > 5:
    number = int(input("Number: "))
```

Award 1 point for converting the first input and 1 point for converting the repeated
input. The loop condition and indentation are already correct.

### 8

`return` is inside the loop, so the function stops at the first matching value. Move
it outside the `for` loop so all values are checked:

```python
def count_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            count = count + 1
    return count
```

Award 1 point for identifying the premature return and 1 point for placing
`return count` after the loop.

## Part 3 - Fill the blanks

- A: `len(values)`
- B: `limit`
- C: `i`
- D: `indexes`

```python
def indexes_at_least(values, limit):
    indexes = []
    for i in range(len(values)):
        if values[i] >= limit:
            indexes.append(i)
    return indexes
```

## Part 4 - One complete answer

```python
scores = [
    [12, 8, 15],
    [10, 17, 9],
    [20, 6, 11],
]

def row_totals(matrix):
    totals = []
    for row in matrix:
        total = 0
        for score in row:
            total = total + score
        totals.append(total)
    return totals

def passing_scores(matrix, limit):
    return [score for row in matrix for score in row if score >= limit]

totals = row_totals(scores)
passing = passing_scores(scores, limit=10)

print(totals)
print(passing)

largest = totals[0]
for total in totals:
    if total > largest:
        largest = total
print(f"Largest row total: {largest}")
```

### Part 4 marking guide

- 1 point: starts a fresh row total at zero for each row;
- 1 point: loops over every score and adds it to the row total;
- 1 point: appends each row total and returns the complete totals list;
- 1 point: uses a double list comprehension in the requested order;
- 1 point: filters scores using `score >= limit` and returns the flat list;
- 1 point: calls and prints both functions, including a keyword argument;
- 1 point: finds the largest row total with a loop and prints 37.

## Use your score to choose what to review

Review the corresponding material for every missed question:

| Missed question | Review |
| --- | --- |
| 1 or 7 | `while`, `break`, input types, and loop conditions |
| 2 | nested loop traces and where counters are updated |
| 3 | order of a double list comprehension and its filter |
| 4 | matrix rows, shallow copies, and copying each row |
| 5 or 6 | function calls, `return`, local names, and mutation |
| 8 or Part 3 | function return position, indexes, and loop scope |
| Part 4 | matrix traversal, accumulators, comprehensions, and function calls |

Use 18-20 as a strong result on the released topics tested here, 14-17 as a sign to
review the missed skills and retake the test, and 0-13 as a prompt to revisit the
related practice stages before trying again. This diagnostic stops at Week 12; add
Week 13 topics to your review once those materials are available.
