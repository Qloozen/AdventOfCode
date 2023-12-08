## Part 1

I was kinda lazy to come up with a smart idea, so I planned to make a simple Hand class. This class contains the cards, hand type as integer, and the bid of the hand.

** Getting the hand type **
The first step is to get the hand type. In my case the best type (Five of a kind) starts from 6, and the worst (High card) is 0. To get this type I keep track of the occurrences of each card in a dictionary and then only used the occurence values per card like QQQJA = [3, 1, 2]. With some lazy if statements you can figure out the hand type.

** Comparing hands **
Now I can compare the hands based on the type. I defined the **gt** method to compare the hands with the > operator and support the sorting of hands. To compare the cards if the types are equal I simply used some more if statements:

```python
for i, card in enumerate(self.cards):
  if card == other.cards[i]: continue
  if cards_order.index(card) < cards_order.index(other.cards[i]): return True
  else: return False
```

With the **gt** method we can just sort the hands, and calculate answer.

## Part 2

I did not change a lot to make part2 work. I simply added the amount of J's to the current highest card occurence, to maximize the hand type. To make J the weakest when comparing the same hand type, I simply extended my **gt** function and let the hand lose if it has a J at some position, unless they both are J's. The same calculation as part 1 is used to calculate the answer.
