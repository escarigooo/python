"""Course week(s): 03, 06-07 | Difficulty: 2/5

Practise cleaning a string and splitting it into words.

Ask for a full name. Remove spaces at the start and end, split the name into a
list called nameparts, then print each part in lowercase on its own line.

Example input: "  Ana de Armas  "
Expected output:
ana
de
armas
"""

name = input("Enter your full name: ")
name = name.strip()
nameparts = name.split()
for i in nameparts:
    print(i.lower())
