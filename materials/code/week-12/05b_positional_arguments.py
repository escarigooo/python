"""Positional arguments: the first argument goes to the first parameter, the second to the second."""

# the definition
def show_pair(a, b):
    print(f"a={a}, b={b}")

# the main part: the same two values, in the two orders
show_pair(3, 5)
show_pair(5, 3)
