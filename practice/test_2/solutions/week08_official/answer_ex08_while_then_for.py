"""Exercise 8 · Predict what it prints

Read the two loops below — a while, then the for you already know.
On paper: write every line the program prints, in order.
Then run it and compare.
"""
i = 0
while i < 3:
    print(i)
    i = i + 1
for i in range(3):
    print(i)

# Answer: 0 1 2 then 0 1 2 — six lines.
# i is reset to 0 when the for loop uses the same name as the while control variable to its own.
# The two loops do the same job; what differs is who manages the counter.
