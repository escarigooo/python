"""Read the program below and write exactly the list it prints. On paper, before any run. Then run it and compare."""

nums = [1, 2, 3, 4]
doubled = [n * 2 for n in nums]
print(doubled)  # [2, 4, 6, 8]
# Every element n becomes n * 2; the comprehension keeps the order of the list it reads.
