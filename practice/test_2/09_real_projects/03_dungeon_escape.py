"""Dungeon Escape: collect a key, open the door, and reach the exit.

Concepts: a matrix as a map, state variables, inventory, while, and conditions.
"""

# Symbols: # wall, P player, K key, D door, T trap, E exit, . floor.
map_rows = [
    "#########",
    "#P..K...#",
    "#.###.#D#",
    "#..T..#E#",
    "#.......#",
    "#########",
]

# Each string becomes a list of characters, producing a mutable matrix.
dungeon = [list(row) for row in map_rows]

player_row = 1
player_column = 1
health = 3
inventory = []
moves = 0
escaped = False

print("DUNGEON ESCAPE")
print("Use W/A/S/D. Find K, open D, and reach E. Avoid T.")

while health > 0 and not escaped:
    print()
    for row in dungeon:
        print("".join(row))
    print(f"Health: {health} | Inventory: {inventory} | Moves: {moves}")

    direction = input("Move: ").strip().upper()

    if direction not in ["W", "A", "S", "D"]:
        print("Please enter W, A, S, or D.")
    else:
        next_row = player_row
        next_column = player_column

        if direction == "W":
            next_row = next_row - 1
        elif direction == "S":
            next_row = next_row + 1
        elif direction == "A":
            next_column = next_column - 1
        else:
            next_column = next_column + 1

        target = dungeon[next_row][next_column]
        allowed_to_move = True

        if target == "#":
            allowed_to_move = False
            print("A wall blocks the way.")
        elif target == "D" and "key" not in inventory:
            allowed_to_move = False
            print("The door is locked. Find the key.")

        if allowed_to_move:
            moves = moves + 1

            if target == "K":
                inventory.append("key")
                print("You collected the key.")
            elif target == "D":
                print("The key opens the door.")
            elif target == "T":
                health = health - 1
                print("Trap! You lose one health.")
            elif target == "E":
                escaped = True

            # Mutate the old cell and the new cell in the matrix.
            dungeon[player_row][player_column] = "."
            player_row = next_row
            player_column = next_column
            dungeon[player_row][player_column] = "P"

print()
for row in dungeon:
    print("".join(row))

if escaped:
    print(f"You escaped in {moves} moves with {health} health!")
else:
    print("You ran out of health.")

