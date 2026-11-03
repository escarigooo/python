# Coding Test 1: three-hour preparation

## What is confirmed

- The test is handwritten. The official preparation version allows 90 minutes;
  confirm the real test's exact duration on Moodle or with the professor.
- No books, notes, computers, or phones are allowed.
- Coding Test 1 covers Weeks 1-7, including `for` loops.
- The official example has four kinds of work:
  1. trace code and choose its output;
  2. find, correct, and explain errors;
  3. fill in missing code;
  4. write complete programs from a description.

The example shows the format, not the secret questions from the real test.

## Use the three hours like this

### 0:00-0:15 — Recall syntax from memory

On paper, write one example of each item without looking at notes:

```python
input()
int()
float()
str()
len()
range()

if condition:
    ...
elif other_condition:
    ...
else:
    ...

for item in collection:
    ...

for index in range(len(values)):
    ...

text.split(",")
text.replace("old", "new")
text.lower()
text.upper()
text.startswith("A")
text.endswith("z")

values.append(item)
item in values
values[start:stop:step]
```

Also write examples using `+`, `-`, `*`, `/`, `//`, `%`, `==`, `!=`, `<`,
`<=`, `>`, `>=`, `and`, `or`, and `not`.

### 0:15-1:45 — Simulate the official test

Print or open `materials/tests/example-coding-test-1.pdf`, but answer every question
on paper. Set a 90-minute timer. Do not run any code and do not read notes.

For tracing questions, make a small table for variables and update it one line at a
time. For programming questions, underline the inputs, outputs, conditions, and
repetitions before writing code.

### 1:45-2:20 — Check and repair

Now type your handwritten answers into Python and run them. For each mistake, write:

1. what Python did;
2. why your answer was wrong;
3. the correct syntax;
4. one new tiny example using the same syntax.

Do not only copy the correction. Rewrite the whole faulty line yourself.

### 2:20-2:45 — Week 7 essentials

Complete Exercises 2, 5, 8, and 9 from
`materials/handouts/week-07-lists-and-for-loops.pdf` on paper first. These practise
list mutation, counters, building lists, indexing, and string/list loops.

Remember these common traps:

```python
# Strings do not change in place.
text = text.replace("-", "")

# append() changes the list and returns None.
names.append("Ana")

# Use indexes when you must replace list elements.
for i in range(len(values)):
    values[i] = values[i] + 1

# Do not remove from the same list you are currently iterating over.
for value in values[:]:
    if value < 0:
        values.remove(value)
```

### 2:45-3:00 — Final paper check

Without notes, write a short program that:

- reads comma-separated integers;
- converts them and stores them in a list;
- counts values matching a condition;
- finds the largest value without using `max()`;
- prints the result with an f-string.

Then check indentation, colons, parentheses, quotation marks, conversions, loop
bounds, and variable names. These small details matter more on paper.

## Minimum knowledge checklist

- Predict types and outputs, especially `input()` returning `str`.
- Convert between `str`, `int`, and `float`.
- Use arithmetic, comparison, Boolean, and membership operators.
- Index and slice strings and lists.
- Use the string methods shown above and remember their return values.
- Build and mutate lists with indexing and `append()`.
- Use `if`/`elif`/`else`, including combined conditions.
- Use `for`, `range()`, counters, accumulators, and nested decisions.
- Find off-by-one errors and explain corrections in words.
- Translate a paragraph into inputs, processing steps, and output.
