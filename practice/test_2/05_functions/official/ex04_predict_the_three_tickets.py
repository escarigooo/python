"""Read the program below — three calls to ticket, with the arguments handed in three ways.
On paper, before any run: write the three printed lines exactly. Then run it and compare.
"""

def ticket(name, seat):
    return name + "-" + seat

print(ticket("Ana", "7"))
print(ticket(seat="7", name="Ana"))
print(ticket("7", "Ana"))
