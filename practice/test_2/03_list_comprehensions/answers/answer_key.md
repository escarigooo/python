# Week 10 answer key

Attempt every official file before reading this page.

## Exercises

1. `[2, 4, 6, 8]`

2.

```python
upper_words = [word.upper() for word in words]
print(upper_words)
```

3.

```python
products = [a * b for a in range(1, 4) for b in range(1, 4)]
print(products)
```

4.

```python
numbers = [int(part) for part in text.split(",")]
print(numbers)
```

5. `[['1', '2'], ['3', '4']]`

6. `[6, 150]`

7.

```python
pairings = [adj + " " + drink for adj in adjs for drink in drinks]
print(pairings)
```

8. `[10, 11, 12, 20, 21, 22]`

9.

```python
above_ten = [number for number in nums if number > 10]
print(above_ten)
```

10. `['SUN', 'SKY']`

11. Both prints show `[10, 20, 30, 40]` because `a` and `b` reference the same
list.

## Recaps

1.

```text
['ada', 'grace', 'ken']
[3, 5, 3] 11
3 d
```

2. Use `text.split(",")` and update the total with `total = total + n`.

3. A: convert every element, then take indexes `0, 2, 4` with `[::2]`.

4.

```text
['GO!', 'GO?', 'RUN!', 'RUN?']
14 GO!
```

5.

```python
names = text.split(";")
long = [n.upper() for n in names if len(n) > 3]
count = 0
for n in long:
    count = count + 1
```

6. A produces `['a1', 'a2', 'c1', 'c2']`.
