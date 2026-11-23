"""Read the program below and write exactly the list it prints, element by element, in order. On paper, before any run. Then run it and compare."""

sums = [a + b for a in [10, 20] for b in range(3)]
print(sums)  # [10, 11, 12, 20, 21, 22]
# a is the outer loop, b the inner; the brackets build one flat list — nothing nests.
