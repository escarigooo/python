"""Exercise 1 · Predict what it prints

Read the while below and write each printed line, and the value of n when the loop stops — trace it by hand.
On paper, before any run. Then run it and compare.
"""
n = 5
while n > 0:
    print(n)
    n = n - 2
# uncomment the next line to check the final value of n
# print(n)

# Answer: 5, 3, 1 — three lines. After printing 1, n becomes -1,
# the condition fails and the loop stops with n = -1.
