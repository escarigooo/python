"""Six operations after b = a: which ones change the list both names share, and which move the name b."""

# row 1 - brackets after the name: the list changes
a = [1, 2, 3]
b = a
b[0] = 5
print(id(a) == id(b), a)

# row 2 - a method: the list changes
a = [1, 2, 3]
b = a
b.append(40)
print(id(a) == id(b), a)

# row 3 - a bare name before the = sign: b moves to a new list
a = [1, 2, 3]
b = a
b = [7]
print(id(a) == id(b), a)

# row 4 - the slice builds a new list
a = [1, 2, 3]
b = a
b = a[:]
print(id(a) == id(b), a)

# row 5 - + builds a new list
a = [1, 2, 3]
b = a
b = b + [40]
print(id(a) == id(b), a)

# row 6 - += changes the list in place
a = [1, 2, 3]
b = a
b += [40]
print(id(a) == id(b), a)
