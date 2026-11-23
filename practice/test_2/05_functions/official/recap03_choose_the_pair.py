"""running_max takes a list of numbers — positive, zero or negative —
and must hand back a new list in which position i holds the largest value of L from position 0 to i:
[3, 1, 4, 2, 5] gives [3, 3, 4, 4, 5], and [-2, -5, -1] gives [-2, -2, -1].
One pair of A to F is right: pick it, and say what each of the others returns instead.
"""

# <X> and <Y> are holes, not Python: the frame is written as comments.
# Put one pair in the holes, remove the # signs of the frame, and run it on the two lists.

# def running_max(L):
#     result = []
#     best = <X>
#     for v in L:
#         best = <Y>
#         result.append(best)
#     return result

#     <X>   <Y>
# A   0     v if v > best else best
# B   L[0]  best if v > best else v
# C   L[0]  v > best
# D   L[0]  v if v > best else best
# E   []    v if v > best else best
# F   L[0]  v if v > best else L[0]
