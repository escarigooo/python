# Rebuild and extension challenges

Use the completed programs as demonstrations, not as answers to memorise. Make a
copy in your own scratch file before changing one.

## 1. Codebreaker

Rebuild a program that gives the player eight attempts to guess `427`.

- Reject guesses that do not have exactly three different digits.
- Say `Exact` for a digit in the correct position.
- Say `Present` for a correct digit in the wrong position.
- Say `None` when no digit occurs in the secret.

Extensions:

1. Change it to a four-digit secret.
2. Store all previous guesses in a list and print them after every turn.
3. Count how many `Exact` and `Present` clues appear instead of listing words.

## 2. Tic-Tac-Toe

Rebuild a two-player 3 by 3 board. Read moves as `row,column`, reject occupied
positions, alternate `X` and `O`, and detect rows, columns, and diagonals.

Extensions:

1. Accept positions 1-3 instead of 0-2.
2. Count victories across repeated games.
3. Create a 4 by 4 version. Which hard-coded diagonal logic must change?

## 3. Dungeon Escape

Rebuild a map where `#` is a wall, `P` the player, `K` a key, `D` a door, `T` a
trap, and `E` the exit. Read `W`, `A`, `S`, or `D` until the player escapes or loses
all health.

Extensions:

1. Add a second key and make opening a door consume one key.
2. Add coins and a score.
3. Add a monster that moves one square after every player move.

## 4. Battleship

Rebuild a 5 by 5 board containing four hidden one-cell ships. The player gets eight
different shots entered as `row,column`. Mark hits with `X` and misses with `O`.

Extensions:

1. Store every shot and print the shot history.
2. Use ships that occupy two adjacent cells.
3. After the game, reveal unhit ships with `S`.

## 5. Game of Life

Rebuild the simulation from these rules:

- a live cell survives with two or three live neighbours;
- a dead cell becomes live with exactly three live neighbours;
- every other cell becomes or remains dead.

Extensions:

1. Ask the user how many generations to simulate.
2. Count and print the living cells in every generation.
3. Stop early if the new grid equals the old grid.
4. Explain why `next_grid = grid` breaks the simulation.

