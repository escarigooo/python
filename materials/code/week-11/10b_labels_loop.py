"""The same three paths as a loop: if, elif and else, one path per line."""

# the data (given in the slide's subtitle)
grades = [18, 9, 12]

# the work
labels = []
for g in grades:
    if g >= 16:
        labels.append("top")
    elif g >= 10:
        labels.append("pass")
    else:
        labels.append("fail")

# the answer
print(labels)
