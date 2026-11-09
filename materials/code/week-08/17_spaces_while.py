"""Count the spaces by index with while: three pieces of bookkeeping."""
s = input("Text: ")
count = 0
i = 0
while i < len(s):
    if s[i] == " ":
        count = count + 1
    i = i + 1
print(count)
