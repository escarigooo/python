"""Three paths in one expression: an if inside an if. It runs, and it is hard to read."""

# the data (given in the slide's subtitle)
grades = [18, 9, 12]

# the work
labels = ["top" if g >= 16
    else "pass" if g >= 10 else "fail"
    for g in grades]

# the answer
print(labels)
