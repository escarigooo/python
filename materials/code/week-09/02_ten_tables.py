"""All ten times tables at once: the outer loop picks the table, the inner one runs it.
"""

for table in range(1, 11):
    for multiplier in range(1, 11):
        print(table * multiplier, end=" ")
    print()
