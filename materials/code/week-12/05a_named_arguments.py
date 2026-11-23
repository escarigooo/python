"""Keyword arguments: each argument names its parameter, and the order stops mattering."""

# the definition
def show_pair(a, b):
    print(f"a={a}, b={b}")

# by position
show_pair(3, 5)
show_pair(5, 3)

# by name
show_pair(a=3, b=5)

# by name, in the other order
show_pair(b=5, a=3)
