"""text = "5 10 15 20 25" is given, and the program ends with print(picked).
Choose the fragment that builds picked — every second number, converted to int —
so the print shows [5, 15, 25].
One of A to D is right: pick it, and say what each of the others does instead.

Uncomment one candidate at a time to run it."""

text = "5 10 15 20 25"

# A
# ns = text.split()
# picked = [int(e) for e in ns][::2]
# B
# ns = text.split()
# picked = [int(e) for e in ns[2:]]
# C
# ns = text.split()
# picked = [int(e) for e in ns][1::2]
# D
# ns = text.split()
# picked = ns[::2]

print(picked)
