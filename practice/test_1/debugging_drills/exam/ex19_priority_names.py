"""EXERCISE 19 — Combined string conditions

A name is Priority when it starts with A, contains silva, or ends with s. The check
must ignore uppercase/lowercase differences.

Expected output for the given list:
Ana: Priority
Bruno: Normal
Rui Silva: Priority
Ines: Priority

Correct the program and explain the Boolean expression.
"""

names = ["Ana", "Bruno", "Rui Silva", "Ines"]

for name in names:
    lowered = name.lower

    if lowered.startswith("a" and "silva" in lowered and lowered.endswith("s")):
        result = "Priority"
    else:
        result = "Normal"

    print(f"{name}: {result}")

