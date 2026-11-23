"""Read the program below and write exactly what it prints —
one line, every character in its place.
On paper, before any run. Then run it and compare."""

words = [["mySQL", "PostgreSQL", "MongoDB"], ["Python", "Assembly", "JAVA"]]
picked = [w for row in words for w in row if len(w) % 2 != 0]
out = ""
for i in range(len(picked)):
    for c in picked[i][::-1]:
        if c.lower() in "aeiou":
            out = out + c.upper()
            break
        out = out + str(i)
    out = out + "-"
print(picked[-1][1:], out)  # ongoDB 00000-11O-
