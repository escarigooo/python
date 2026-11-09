"""Count the spaces directly with for: the loop hands you each character."""
s = input("Text: ")
count = 0
for c in s:
    if c == " ":
        count = count + 1
print(count)
