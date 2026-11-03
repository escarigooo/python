"""EXERCISE 7 — Strings are immutable

Remove spaces and hyphens and print a lowercase username.

For full_name = "Ana Maria-Silva"
Expected output: anamariasilva

Correct every faulty line and explain why replace() must be assigned.
"""

full_name = "Ana Maria-Silva"
new_name = full_name.replace(" ", "")
new_name = new_name.replace("-", "")
username = new_name.lower()
print(username)

# Needs to save in a new variable 