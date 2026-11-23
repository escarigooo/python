"""Two paths in one expression: the even numbers are doubled, the odd ones turn negative."""

# the data
nums = [3, 8, 5, 12]

# the work
changed = [n * 2 if n % 2 == 0 else -n for n in nums]

# the answer
print(changed)
