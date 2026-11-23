"""Read the program below and write exactly the two printed lines, in order.
On paper, before any run. Then run it and compare."""

a = [1, 2, 3]
b = a
c = a[:]
a.append(4)
print(b)  # [1, 2, 3, 4] - b is a second name for the list of a
print(c)  # [1, 2, 3] - the slice built a new list before the append
