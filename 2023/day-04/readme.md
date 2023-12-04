## Part 1

For part one I simply splitted the two lists of all cards into tuples `(winning_numbers, numbers)`. I converted these lists into Sets to make the intersection operation easier to get the amount of matching numbers. Since each matching number doubles the score and we start from 1 we can use this to calculate the score:

```python
2 ** (intersection_amount - 1)
```

We append each score to the answer and print out the result.

## Part 2

For part two I extended the tuple of part 1 : `(amount, winning_numbers, numbers)`. I initialize each card with an amount of 1 since we start with atleast the original card. So the rules are stating that the amount of matching numbers is the amount of copies you make from the card below the current one.

**Iteration 1:**
| From                            | To                           |
| ------------------------------- | ---------------------------- |
| Card 1 (amount: 1, matching: 2) | Card 1 (amount: 1)           |
| Card 2 (amount: 1)              | Card 2 (amount: 2) # +1 copy |
| Card 3 (amount: 1)              | Card 3 (amount: 2) # +1 copy |


**Iteration 2:**
| From                            | To                                            |
| ------------------------------- | ----------------------------------------------|
| Card 1 (amount: 1)              | Card 1 (amount: 1)                            |
| Card 2 (amount: 2, matching: 2) | Card 2 (amount: 2)                            |
| Card 3 (amount: 2)              | Card 3 (amount: 3) # +1 copy                  |
|                                 | # second copy falls out of the range of cards |

**Iteration 3:**
- same as iteration 2, since it is a copy of card 2

**Iteration 4, 5, 6, 7:**
- We have now 4 copies of card 3, so we have 4 iterations, but none will make copies because it is the last card.

So I simply iterate over the current amount of cards (1x for card 1 since we can't make copies of past cards). Then I make copies of all the following cards with this function:

```python
def make_copies(start, amount):
  for j in range(0, amount):
    if start + j >= len(input): break
    card = input[start + j]
    input[start + j] = (card[0] + 1, card[1], card[2]) # since tuples are immutable we have to create a new one with the copy added
```

In the end we count the amount of cards we have (including the copies) and print out the result.
