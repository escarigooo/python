"""A small, single-player Battleship game.

Concepts: matrices, hidden data, coordinate validation, membership, and counters.
"""

size = 5

# This is a double list comprehension: make 5 rows, each containing 5 dots.
board = [["." for column in range(size)] for row in range(size)]

# The ship coordinates are hidden from the player while the game runs.
ships = [[0, 1], [2, 3], [3, 0], [4, 4]]
maximum_shots = 8
shots = 0
hits = 0

print("MINI BATTLESHIP")
print("Find four ships on a 5 by 5 board in eight different shots.")
print("X = hit, O = miss, . = unknown")

while shots < maximum_shots and hits < len(ships):
    print("\n  0 1 2 3 4")
    for row in range(size):
        print(f"{row} " + " ".join(board[row]))

    while True:
        coordinates = input("Fire at row,column: ").split(",")
        valid_shot = True

        if len(coordinates) != 2:
            valid_shot = False
        elif not coordinates[0].strip().isdigit() or not coordinates[1].strip().isdigit():
            valid_shot = False
        else:
            row = int(coordinates[0].strip())
            column = int(coordinates[1].strip())

            if row < 0 or row >= size or column < 0 or column >= size:
                valid_shot = False
            elif board[row][column] != ".":
                valid_shot = False
                print("You already fired there.")

        if valid_shot:
            break
        print("Enter a new coordinate from 0 to 4, such as 2,3.")

    shots = shots + 1

    if [row, column] in ships:
        board[row][column] = "X"
        hits = hits + 1
        print("Hit!")
    else:
        board[row][column] = "O"
        print("Miss.")

    print(f"Hits: {hits}/{len(ships)} | Shots left: {maximum_shots - shots}")

print("\nFINAL BOARD")
print("  0 1 2 3 4")
for row in range(size):
    # Reveal every ship that was not hit.
    for column in range(size):
        if [row, column] in ships and board[row][column] == ".":
            board[row][column] = "S"
    print(f"{row} " + " ".join(board[row]))

if hits == len(ships):
    print("You sank the fleet!")
else:
    print(f"Game over. You found {hits} of {len(ships)} ships.")

