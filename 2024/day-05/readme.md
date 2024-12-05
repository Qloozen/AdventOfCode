## Part 1

> The goal is to find the updates that are sorted correctly, and then taking the middle value of an update and sum them up. The input has two sections, one with ordering rules "X|Y", which indicate a page number X need to come before Y. Section two is a list of updates, a single update is a list op page numbers. For part 1 we can ignore the updates that are not sorted correctly.

```plaintext
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```

### Solution

1. First i store the ordering rules in tuples like this `[(X, Y), ...]`. The updates are simply stored as lists of page numbers.

```python
with open("input.txt") as f:
    ordering_rules, updates = f.read().split("\n\n")
    ordering_rules = [tuple(map(int, rule.split("|"))) for rule in ordering_rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]
```

2. Only rules where both X and Y are in the update are considered. I then check if the update follows this rule by checking the index of X and Y in the update. If X comes before Y in the update, The update follows this rule correctly.

I have wrapped this in a list, and check if **all** of the rules are followed. If they are, I add the middle value of the update to the sum.

```python
part1, part2 = 0, 0
for update in updates:
  is_ordered = all([update.index(x) < update.index(y) for x, y in ordering_rules if x in update and y in update])

  if is_ordered: part1 += update[len(update)//2]
```

## Part 2

> The goal now is to only condider the unordered updates. Same as part 1 we need to get the middle page number of the update, but before this we need to sort the update, based on the sorting_rules.

### Solution

1. First i started to create a sorting function that compares two given numbers. Since i stored the rules as (X, Y) tuples, I can check if the given numbers (a, b) are in the rules, if it is, we now that the given order is correct. Then we could also say that if (b, a) if in the rules, the order is incorrect. If none of these are in the rules, we can't say anything about the order.

```python
    def sortFn(a, b): # for part 2
        if (a, b) in ordering_rules: return -1
        elif (b, a) in ordering_rules: return 1
        else: return 0
```

2. To use this compare function in the built-in sorting function, I used the cmp_to_key function from functools. After this we do the same as part 1.

```python
    for update in updates:
        is_ordered = all([update.index(x) < update.index(y) for x, y in ordering_rules if x in update and y in update])

        if is_ordered: # part 1 ...
        else: # part 2
            update_sorted = sorted(update, key=cmp_to_key(sortFn))
            part2 += update_sorted[len(update_sorted)//2]
```
