"""Read the program below and write the exact lines it prints, in order, and say how many there are.
On paper, before any run. Then run it and compare.
"""

for i in range(3):
    for j in range(i):
        print(i, j)

# The program prints three lines:
# 1 0
# 2 0
# 2 1

# The first outer step runs range(0), an empty sequence, so the
# inner body does not run at all — six lines is the wrong answer.
