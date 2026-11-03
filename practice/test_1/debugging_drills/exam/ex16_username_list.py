"""EXERCISE 16 — Strings, lists, and duplicate usernames

Create one lowercase username per semicolon-separated full name. Remove spaces and
hyphens. Store each username only once.

For raw_names = "Ana Silva;Joao-Pedro;Ana Silva"
Expected output: ['anasilva', 'joaopedro']

Correct all faulty lines and explain them.
"""

raw_names = "Ana Silva;Joao-Pedro;Ana Silva"
names = raw_names.split()
usernames = []

for name in names:
    username = name.replace(" ", "")
    username.replace("-", "")
    username.lower()

    if username in names:
        usernames.append(username)

print(usernames)

