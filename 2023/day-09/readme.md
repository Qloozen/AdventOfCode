# Part 1

A history sequence is a list of numbers like `[1, 3, 6, 10, 15, 21]`. To find the next number in this sequence (our goal), we need to find the sequences below it which are the steps between each number. So the sequence below = `[2, 3, 4, 5, 6]`, till we reach the point where you end up with all zeros, in this case `[0, 0, 0]`.

To each sequence, we add a next number to it. We start at the end with the `[0, 0, 0]` sequence, which always gets a 0 added to it. The next number of the sequence above is the sum of it's last number + last number of the sequence below (which is the 0 we've just added). This repeats for all sequences till we reach the top. We end up with the next number: `[1, 3, 6, 10, 15, 28]`. **28** is the next number in the sequence.

We sum all the numbers for each history sequence in the input.

**Solution is included with part2**

# Part 2

We will do the same thing as above, but now we want to know the first value of each sequence. Same rules apply, only we subtract the values instead of adding them. Below you can see an example of a history sequence. Left side is part 2, right side is part 1.

```
(5)  10  13  16  21  30  45  (68)
  (5)   3   3   5   9  15  (23)
    (-2)  0   2   4   6  (8)
      (2)   2   2   2  (2)
        (0)   0   0  (0)
```

To solve this I use a recursive function. The base case is when you hit the all-zero sequence. The values are both always 0, as you see in the example above, so i return (0, 0). For the input sequence you first need to get the extrapolated values of the sequence below it, we call the same function with the next sequence. In the end I return a tuple with the left values (part2) and right values (part1). Below is the recursive function:

```python
def get_hist_values(s):
    if all([x == 0 for x in s]): return (0, 0) # left (part2), right (part1)
    next_seq = [s[step+1] - s[step] for step in range(len(s)-1)]
    x = get_hist_values(next_seq)
    return (s[0] - x[0], s[-1] + x[1])
```

In the end we sum all the left values for part 2 and all the right values for part 1:

```python
hist = [get_hist_values(sequence) for sequence in input]
extrapolated_values = reduce(lambda acc, x: (acc[0] + x[0], acc[1] + x[1]), hist)
```
