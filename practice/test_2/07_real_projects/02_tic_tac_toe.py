"""Two-player Tic-Tac-Toe without functions.

Concepts: matrices, nested loops, validation, counters, and game state.
"""

# A matrix is a list whose items are also lists.
# board[row][column] selects one cell.
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

player = "X"
winner = ""
moves = 0

print("TIC-TAC-TOE")
print("Enter a row and column from 0 to 2, for example: 1,2")

while winner == "" and moves < 9:
    print("\n  0   1   2")
    for row in range(len(board)):
        print(f"{row} {board[row][0]} | {board[row][1]} | {board[row][2]}")
        if row < len(board) - 1:
            print("  --+---+--")

    # Keep asking until this player gives a valid, free coordinate.
    while True:
        raw_move = input(f"Player {player}, row,column: ").split(",")
        valid_move = True

        if len(raw_move) != 2:
            valid_move = False
        elif not raw_move[0].strip().isdigit() or not raw_move[1].strip().isdigit():
            valid_move = False
        else:
            row = int(raw_move[0].strip())
            column = int(raw_move[1].strip())

            if row < 0 or row >= 3 or column < 0 or column >= 3:
                valid_move = False
            elif board[row][column] != " ":
                valid_move = False
                print("That cell is already occupied.")

        if valid_move:
            break

        print("Use two free coordinates from 0 to 2, such as 1,2.")

    board[row][column] = player
    moves = moves + 1

    # Check all rows. The counter must be reset for each new row.
    for row_index in range(3):
        matching = 0
        for column_index in range(3):
            if board[row_index][column_index] == player:
                matching = matching + 1
        if matching == 3:
            winner = player

    # Check all columns.
    for column_index in range(3):
        matching = 0
        for row_index in range(3):
            if board[row_index][column_index] == player:
                matching = matching + 1
        if matching == 3:
            winner = player

    # Check the two diagonals.
    main_diagonal = 0
    other_diagonal = 0
    for index in range(3):
        if board[index][index] == player:
            main_diagonal = main_diagonal + 1
        if board[index][2 - index] == player:
            other_diagonal = other_diagonal + 1

    if main_diagonal == 3 or other_diagonal == 3:
        winner = player

    # Change player only when another turn will be played.
    if winner == "":
        if player == "X":
            player = "O"
        else:
            player = "X"

# Show the final board.
print("\n  0   1   2")
for row in range(3):
    print(f"{row} {board[row][0]} | {board[row][1]} | {board[row][2]}")
    if row < 2:
        print("  --+---+--")

if winner == "":
    print("Draw: every cell is occupied.")
else:
    print(f"Player {winner} wins!")

