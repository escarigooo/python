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
