"""The sequence can be a string: for hands out one letter at a time, the expression capitalises each one."""

word = "python"
capitals = [ch.upper() for ch in word]
print(capitals)