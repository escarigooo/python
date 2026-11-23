"""Recap 2 · Choose the fragment

The program should print the letters of word, one per line, walking the string by its index — and then print i.
It starts with word = "loop" and i = 0, and ends with print(i). Exactly one of the four fragments below does the job.
Choose it — and say what goes wrong in each of the other three.
"""
word = "loop"
i = 0
# A — the answer: prints l, o, o, p on four lines, then 4
while i < len(word):
    print(word[i])
    i = i + 1
# B — tests i <= len(word): after the p it asks for word[4] — IndexError.
# while i <= len(word):
#     print(word[i])
#     i = i + 1
# C — steps before it reads: skips the l, prints o o p, then word[4] — IndexError.
# while i < len(word):
#     i = i + 1
#     print(word[i])
# D — never moves i: i + 1 is computed and thrown away (week 7’s reset 2);
# the condition stays true and the l prints forever — trap 02. Do not run it.
# while i < len(word):
#     print(word[i])
#     i + 1
print(i)
