"""The filter: an if at the end chooses what enters the list. The slide's folded forms with their colons are scaffolding, not Python — this file carries the final line only. Type print(evens) to see the list: [4, 2]."""

nums = [4, 7, 2, 9, 1]
evens = [n for n in nums if n % 2 == 0]
