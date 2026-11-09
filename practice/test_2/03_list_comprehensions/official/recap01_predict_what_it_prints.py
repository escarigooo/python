"""Read the program below and write exactly what it prints — every line, in order.
On paper, before any run. Then run it and compare."""

words = "ada grace ken"
names = words.split()
sizes = [len(n) for n in names]
total = 0
for n in sizes:
    total = total + n
print(names)
print(sizes, total)
print(n, names[0][1])
