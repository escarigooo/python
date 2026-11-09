"""Read the program below and write exactly what it prints — every line, in order.
On paper, before any run. Then run it and compare."""

words = ["go", "run"]
ends = ["!", "?"]
shouts = [w.upper() + e for w in words for e in ends]
total = 0
for s in shouts:
    total = total + len(s)
print(shouts)
print(total, shouts[0])
