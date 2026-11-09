"""The capped game with for: range(3) caps the turns, break leaves on the right guess."""
secret = 7
for attempt in range(3):
    guess = int(input("Guess: "))
    if guess == secret:
        print("You got it!")
        break
