"""Write a program for the 5-by-5 multiplication grid — the products i × j, for i and j from 1 to 5 — that prints, for each row, how many of its products are even, exactly as the output below shows. Use this lecture’s nested for loops, with a counter — and decide with care where the counter starts again.

The output to produce:
>>> 2
>>> 5
>>> 2
>>> 5
>>> 2
"""

for i in range(1, 6):
    count = 0
    for j in range(1, 6):
        if (i * j) % 2 == 0:
            count = count + 1
    print(count)

# The program prints:
# 2
# 5
# 2
# 5
# 2

# count = 0 sits inside the outer loop, because the count starts
# again on every row.
