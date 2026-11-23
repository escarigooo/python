"""Conway's Game of Life, simulated for a fixed number of generations.

Concepts: matrices, four nested loops, neighbour counting, and next state.
"""

# 1 means alive and 0 means dead. This pattern begins as a "glider".
grid = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

generations = 8
generation = 0
height = len(grid)
width = len(grid[0])

print("CONWAY'S GAME OF LIFE")
print("# = alive, . = dead")

while generation < generations:
    print(f"\nGeneration {generation}")

    for row in range(height):
        line = ""
        for column in range(width):
            if grid[row][column] == 1:
                line = line + "#"
            else:
                line = line + "."
        print(line)

    # IMPORTANT: every generation needs a separate matrix.
    # `next_grid = grid` would give two names to the same mutable list.
    next_grid = [[0 for column in range(width)] for row in range(height)]

    for row in range(height):
        for column in range(width):
            living_neighbours = 0

            # Offsets -1, 0, 1 examine the eight cells around this cell.
            for row_change in range(-1, 2):
                for column_change in range(-1, 2):
                    neighbour_row = row + row_change
                    neighbour_column = column + column_change

                    is_current_cell = row_change == 0 and column_change == 0
                    is_inside = (
                        neighbour_row >= 0
                        and neighbour_row < height
                        and neighbour_column >= 0
                        and neighbour_column < width
                    )

                    if not is_current_cell and is_inside:
                        living_neighbours = living_neighbours + grid[neighbour_row][neighbour_column]

            # Survival: a live cell remains alive with two or three neighbours.
            if grid[row][column] == 1 and living_neighbours in [2, 3]:
                next_grid[row][column] = 1
            # Birth: a dead cell becomes alive with exactly three neighbours.
            elif grid[row][column] == 0 and living_neighbours == 3:
                next_grid[row][column] = 1

    grid = next_grid
    generation = generation + 1

print("\nNow change the initial pattern or the number of generations.")

