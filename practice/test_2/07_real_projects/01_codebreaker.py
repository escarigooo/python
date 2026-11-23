"""Codebreaker: guess a three-digit secret using positional clues.

Concepts: input, validation, while, break, nested loops, strings, and lists.
"""

print("CODEBREAKER")
print("Guess the three different digits.")
print("Exact = right digit and position")
print("Present = right digit, wrong position")
print("None = none of the digits occur in the secret")

# The secret is fixed so the program needs no module that is outside the syllabus.
# TRY: change this after you understand the complete program.
secret = "427"
maximum_attempts = 8
attempt = 0
won = False

while attempt < maximum_attempts:
    # This inner loop repeats until the user gives one valid guess.
    while True:
        guess = input("Guess: ").strip()
        valid = True

        if len(guess) != len(secret) or not guess.isdigit():
            valid = False
            print("Enter exactly three digits.")
        else:
            # LOGIC: compare every position with every later position.
            # If two positions contain the same digit, the guess is invalid.
            for first in range(len(guess)):
                for second in range(first + 1, len(guess)):
                    if guess[first] == guess[second]:
                        valid = False

            if not valid:
                print("Use three different digits.")

        if valid:
            break

    attempt = attempt + 1

    if guess == secret:
        print(f"Correct in {attempt} attempts!")
        won = True
        break

    clues = []

    # A string is a sequence, so guess[position] accesses one character.
    for position in range(len(guess)):
        if guess[position] == secret[position]:
            clues.append("Exact")
        elif guess[position] in secret:
            clues.append("Present")

    if len(clues) == 0:
        print("None")
    else:
        # join() combines a list of strings with a separator between the items.
        print(" | ".join(clues))

    remaining = maximum_attempts - attempt
    print(f"Attempts remaining: {remaining}")

if not won:
    print(f"Game over. The secret was {secret}.")

