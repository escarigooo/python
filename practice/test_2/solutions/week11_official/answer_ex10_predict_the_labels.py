"""Read the program below and write exactly the list it prints.
On paper, before any run. Then run it and compare."""

grades = [14, 8, 17]
labels = ["pass" if g >= 10 else "fail" for g in grades]
print(labels)  # ['pass', 'fail', 'pass']
