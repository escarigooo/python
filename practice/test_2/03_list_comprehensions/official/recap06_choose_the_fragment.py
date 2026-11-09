"""letters = "abc" is given, and the program ends with print(pairs).
Choose the fragment that builds pairs — every letter joined to every digit of "12",
skipping the letter "b" — so the print shows ['a1', 'a2', 'c1', 'c2'].
One of A to D is right: pick it, and say what each of the other three prints instead.

Uncomment one candidate at a time to run it."""

letters = "abc"

# A
# pairs = [L + d for L in letters for d in "12" if L != "b"]
# B
# pairs = [L + d for d in "12" for L in letters if L != "b"]
# C
# pairs = [L + d for L in letters for d in "12" if L == "b"]
# D
# pairs = [L for L in letters for d in "12" if L != "b"]

print(pairs)
