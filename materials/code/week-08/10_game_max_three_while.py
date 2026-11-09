"""The capped game with while: the counter set, tested and stepped by hand; break leaves on the right guess."""
secret = 7
attempts = 0
while attempts < 3:
    guess = int(input("Guess: "))
    if guess == secret:
        print("You got it!")
        break
    attempts = attempts + 1
