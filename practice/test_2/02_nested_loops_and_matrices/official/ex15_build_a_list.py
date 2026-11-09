"""Read the program in the panel, predict the list it prints, then run it and compare.
It works — count the lines it takes to build one list from three values.
"""

names = ["Ada", "Grace", "Ken"]
lengths = []
for name in names:
    lengths.append(len(name))
print(lengths)
