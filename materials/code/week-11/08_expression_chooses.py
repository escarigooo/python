"""A conditional expression inside a comprehension: it decides what each element becomes."""

# the data
nums = [4, -7, 2, -9]

# the work
absolutes = [n if n >= 0 else -n for n in nums]

# the answer
print(absolutes)
