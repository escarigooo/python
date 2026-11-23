"""text = "5 10 15 20 25" is given, and the program ends with print(picked). Choose the fragment that builds picked — every second number, converted to int — so the print shows [5, 15, 25]. One of A to D is right: pick it, and say what each of the others does instead."""

text = "5 10 15 20 25"

# A — the answer: split, convert every piece, then the step slice keeps positions 0, 2, 4
ns = text.split()
picked = [int(e) for e in ns][::2]

# B — ns[2:] is not 'every second': everything from position 2 on -> [15, 20, 25]. Runs and lies.
# ns = text.split()
# picked = [int(e) for e in ns[2:]]

# C — the step slice starts one position late: [1::2] keeps positions 1 and 3 -> [10, 20]. Runs and lies.
# ns = text.split()
# picked = [int(e) for e in ns][1::2]

# D — the conversion is missing: ['5', '15', '25'] — the quotes are the tell. Runs and lies.
# ns = text.split()
# picked = ns[::2]

print(picked)  # [5, 15, 25]
