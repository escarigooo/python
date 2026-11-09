"""The game resolved: the while keeps asking until the guess is right."""
secret = 7
guess = int(input("Guess: "))
while secret != guess:
    guess = int(input("Try again: "))
print("You got it!")
