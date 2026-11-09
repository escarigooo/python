"""Exercise 15 from lecture 9, replayed: three lines to build one list, one element at a time."""

names = ["Ada", "Grace", "Ken"]
lengths = []
for name in names:
    lengths.append(len(name))
print(lengths)
