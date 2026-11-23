"""Read the program below and write exactly what it prints — every line, in order.
On paper, before any run. Then run it and compare.
"""

def area(w, h):
    print(f"area {w} {h}")
    return w * h

def show(v):
    print(f"show {v}")

x = area(h=2, w=5)
y = show(area(3, x))
z = [area(n, n) for n in range(1, x, 4) if n > 1]
print(f"{x} {y} {z}")
