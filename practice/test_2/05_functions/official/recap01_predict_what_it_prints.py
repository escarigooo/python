"""Read the program below and write exactly what it prints — one line, every character in its place.
On paper, before any run. Then run it and compare.
"""

def build(n):
    return [[r * c for c in range(r, n)] for r in range(1, n)]

M = build(4)
out = ""
for row in M:
    for v in row[::-1]:
        if v % 2 == 0:
            out = out + str(v)
        else:
            break
    out = out + "|"
print(len(M), out)
