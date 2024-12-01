## Part 1

The goal is to pair up each number of the left list with a number from the right list. Both lists need to be sorted to create the correct pairs. Finally, we need to add up all the differences between the pairs.

step 1: read the input file and get the left and right list.

```
3   4
4   3
2   5
1   3
3   9
3   3
```

```python
l, r = map(list, zip(*(map(int, line.split()) for line in f.read().splitlines())))
```

above reads every line from the input, splitting each line on the white space, resulting in eg. `['3', '4']` on each line. The `map(int, ...)` converts this list of string to a list of integers.

The `zip(*...)` will transpose the list of pairs, resulting in two lists, one for the left and one for the right. The `*` is used to unpack the list of pairs into the `zip` function.

step 2: sort both lists and sum up the difference between each pair

```python
ans1 = sum(abs(r-l) for l, r in zip(sorted(l), sorted(r)))
```

## Part 2

The goal is now to find the similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

step 1: from the left and right list, from part 1, I find the intersection (numbers that appear in both lists)

```python
sim = list(set(l) & set(r))
```

step 2: finally I iterate over the intersection numbers, multiplying the number by the number of times it appears in the right list, and then multiplying that by the number of times it appears in the left list. Then sum this result.

```python
ans2 = sum(i * r.count(i) * l.count(i) for i in sim)
```
