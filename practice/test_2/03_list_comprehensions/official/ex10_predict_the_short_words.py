"""Read the program below and write exactly the list it prints.
On paper, before any run. Then run it and compare."""

words = ["sun", "moon", "sky", "star"]
short = [w.upper() for w in words if len(w) == 3]
print(short)
