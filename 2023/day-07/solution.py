from functools import reduce

part2 = False
cards_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

class Hand():
  def __init__(self, cards, bid) -> None:
    self.cards = cards
    self.bid = int(bid)
    self.getHandType()
  
  def getHandType(self):
    card_occurrences = reduce(lambda acc, char: {**acc, char: acc.get(char, 0) + 1}, self.cards, {})
    
    if part2:
      J_amount, card_occurrences['J'] = card_occurrences.get('J', 0), 0 # part 2
      sorted_occurrences = sorted(card_occurrences.values(), reverse=True)
      sorted_occurrences[0] = sorted_occurrences[0] + J_amount
    else:
      sorted_occurrences = sorted(card_occurrences.values(), reverse=True)

    if sorted_occurrences[0] == 5: self.hand_type = 6 # Five of a kind
    elif sorted_occurrences[0] == 4: self.hand_type = 5 # Four of a kind
    elif sorted_occurrences[0] == 3 and sorted_occurrences[1] == 2: self.hand_type = 4 # Full house
    elif sorted_occurrences[0] == 3: self.hand_type = 3 # Three of a kind
    elif sorted_occurrences[0] == 2 and sorted_occurrences[1] == 2: self.hand_type = 2 # Two pair
    elif sorted_occurrences[0] == 2: self.hand_type = 1 # One pair
    else: self.hand_type = 0 # High card

  def __gt__(self, other):
    if self.hand_type > other.hand_type : return True
    elif self.hand_type == other.hand_type:
      for i, card in enumerate(self.cards):
        if card == other.cards[i]: continue
        if part2 and card == 'J': return False # part 2
        if part2 and other.cards[i] == 'J': return True  # part 2
        if cards_order.index(card) < cards_order.index(other.cards[i]): return True
        else: return False
    else: return False

with open("2023/day-07/input.txt") as f:
  hands = [Hand(*line.split()) for line in f.readlines()]

ans = sum((i + 1) * hand.bid for i, hand in enumerate(sorted(hands)))
print(ans)

part2 = True
for hand in hands: hand.getHandType() # resetting hand types
ans2 = sum((i + 1) * hand.bid for i, hand in enumerate(sorted(hands)))
print(ans2)

#Your puzzle answer was 250474325.
#Your puzzle answer was 248909434.


