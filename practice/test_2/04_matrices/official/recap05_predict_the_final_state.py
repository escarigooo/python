"""Read the program below — it prints nothing. On paper, before any run:
write the final values of nums and moved, and how many times the body of the while loop executes.
Then add two prints and a counter, run it and compare."""

nums = [4, 9, 2, 6, 7]
moved = []
i = 0
while len(nums) > 2:
    if nums[i] % 2 == 0:
        moved.append(nums.pop(i))
    else:
        i = i + 1
    if i >= len(nums):
        break
