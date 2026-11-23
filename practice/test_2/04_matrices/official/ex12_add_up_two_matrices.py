"""Run the program — the total of A.
Now do the same for B, and print which total is bigger, using what has been taught so far —
and notice which names you are allowed to reuse."""

A = [[1, 2], [3, 4]]
total = 0
for row in A:
    for value in row:
        total = total + value
print(total)
