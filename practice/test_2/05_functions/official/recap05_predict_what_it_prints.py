"""Read the program below and write exactly the line it prints. On paper, before any run —
keep a table of n and count, turn by turn. Then run it and compare.
"""

def steps(n, limit):
    count = 0
    while n != 1 and count < limit:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count = count + 1
    return count

n = 6
a = steps(n, 20)
b = steps(limit=3, n=a)
print(n, a, b)
