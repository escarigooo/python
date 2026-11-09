# Coding Test 2 preparation

Coding Test 2 is scheduled for **5 December 2026**. The official course plan covers
Weeks 8-13:

1. `while` and `break`;
2. nested loops;
3. list comprehensions;
4. matrices;
5. functions: definition, call, and `return`;
6. functions: parameters and scope.

The supplied archive currently reaches Week 10. This workspace contains everything
released through that point and reserves the remaining path for Weeks 11-13.

## Study order

| Stage | Folder | Goal |
| --- | --- | --- |
| 1 | `01_while_and_break` | Control an unknown number of repetitions safely |
| 2 | `02_nested_loops_and_matrices` | Trace two counters and process every matrix cell |
| 3 | `03_list_comprehensions` | Translate loops into comprehensions and back |
| 4 | `04_complex_practice` | Combine the topics in complete programs |
| 5 | `05_debugging` | Find and explain exam-style faults |
| 6 | `06_mock_test` | Work on paper under a timer |

## The mastery rule

For every exercise:

1. predict or design the answer on paper;
2. explain every loop using plain language;
3. run the program only after the paper attempt;
4. record the mistake, its cause, and the corrected rule;
5. repeat failed exercises after 1, 3, and 7 days.

Do not read `solutions/` until two honest attempts have failed. A correct program is
not mastered until you can reproduce it without notes and explain every line.

## Current 20/20 checkpoint

Before Weeks 11-13 arrive, you should be able to do all of the following from memory:

- initialise, test, and update a `while` loop;
- prove why a loop stops and recognise an infinite loop;
- use `break` inside `if` without skipping required work;
- trace nested loops in exact execution order;
- distinguish rows, columns, `m[i]`, and `m[i][j]`;
- reset counters at the correct nesting level;
- build, read, and mutate nested lists;
- translate a loop with `append()` into a list comprehension;
- read double comprehensions from left to right;
- filter a comprehension with a final `if`;
- explain list aliasing (`b = a`) versus copying (`b = a[:]`).
