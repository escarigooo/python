"""Count only the spaces in the first sentence -- the for version, stopped by break."""
s = input("Text: ")
count = 0
for c in s:
    if c == ".":
        break
    if c == " ":
        count = count + 1
print(count)
