# Real projects using Coding Test 2 syntax

These are complete, playable terminal projects. They are intentionally written with
the material released through Week 10: variables, strings, lists, conditions,
`for`, `while`, `break`, nested loops, matrices, and list comprehensions.

There are no user-defined functions or classes yet. In a professional project we
would use them to divide the program into smaller parts, but that would hide the
syntax you currently need to practise.

## Run the projects

From the repository root:

```bash
python3 practice/test_2/07_real_projects/01_codebreaker.py
python3 practice/test_2/07_real_projects/02_tic_tac_toe.py
python3 practice/test_2/07_real_projects/03_dungeon_escape.py
python3 practice/test_2/07_real_projects/04_battleship.py
python3 practice/test_2/07_real_projects/05_game_of_life.py
```

## Learning order

| Project | Difficulty | What it makes real |
| --- | --- | --- |
| Codebreaker | 2/5 | validation, `while`, `break`, string indexing |
| Tic-Tac-Toe | 3/5 | a matrix, coordinates, row/column checks |
| Dungeon Escape | 3/5 | game state, movement, inventory, a map matrix |
| Battleship | 4/5 | hidden data versus displayed data, coordinates |
| Game of Life | 5/5 | four nested loops, neighbours, next-state matrix |

## The three-pass method

Do not only read the programs.

1. **Play:** run a project and understand the rules.
2. **Trace:** choose one turn and write every changed variable on paper.
3. **Rebuild:** close the completed file and recreate it from the specification in
   `CHALLENGES.md`. Compare only after your program runs.

In every file, read the comments beginning with `SYNTAX`, `LOGIC`, and `TRY`:

- `SYNTAX` explains a Python rule;
- `LOGIC` explains why the program needs that block;
- `TRY` gives you a safe modification to make.

The projects are original course-level implementations. `SOURCES.md` lists the
established educational repositories that inspired the choice of project ideas.

