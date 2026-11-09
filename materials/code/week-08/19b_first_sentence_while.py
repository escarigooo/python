"""Count only the spaces in the first sentence -- the while whose condition does the stopping."""
s = input("Text: ")
count = 0
i = 0
while i < len(s) and s[i] != ".":
    if s[i] == " ":
        count = count + 1
    i = i + 1
print(count)
