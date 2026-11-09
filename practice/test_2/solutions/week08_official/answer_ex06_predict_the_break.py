"""Exercise 6 · Predict what it prints

Read the loop below and write exactly which numbers print, and say at which value the loop ends.
On paper, before any run, then run it and compare.
"""
for n in [3, 6, 9, 12]:
    if n > 8:
        break
    print(n)

# Answer: 3, 6 — two lines.
# At 9 the test n > 8 is true, so break stops the loop before the print.
