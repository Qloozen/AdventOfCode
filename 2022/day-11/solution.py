class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspection_count = 0
    def __throw(self, worry_level) -> int:
        return self.true if worry_level % self.test == 0 else self.false

    def inspect(self, mod):
        self.inspection_count += 1
        item = self.items.pop(0)
        worry_level = eval(self.get_eval(item))
        # part 1: divide by 3, part 2: take modulo instead
        worry_level = worry_level // 3 if mod == None else worry_level % mod
        next_monkey = self.__throw(worry_level)
        return (next_monkey, worry_level)

    def get_eval(self, worry_level):
        return self.operation.replace('old', str(worry_level))

    def add_item(self, item):
        self.items.append(item)

    def reset_items(self, items):
        self.items = items

    def reset_inspection_count(self):
        self.inspection_count = 0

from functools import reduce
from typing import List
with open("day-11/input.txt") as f:
    input = [monkey.splitlines() for monkey in  f.read().split('\n\n')]
    monkeys: List[Monkey] = []
    for monkey_input in input:
        items = [int(i) for i in monkey_input[1].split(': ')[1].split(', ')]
        operation = monkey_input[2].split('= ')[1]
        test = int(monkey_input[3].split('by ')[1])
        true = int(monkey_input[4].split('monkey ')[1])
        false = int(monkey_input[5].split('monkey ')[1])
        monkey = Monkey(items, operation, test, true, false)
        monkeys.append(monkey) 

modulo = 1 # used in part 2
modulo = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys]) 

# part 1
for i in range(20):
    for m in range(len(monkeys)):
        monkey = monkeys[m]       
        for _ in range(len(monkey.items)):
            next_monkey, worry_level = monkey.inspect(None)
            monkeys[next_monkey].add_item(worry_level)
two_most_active = list(sorted([monkey.inspection_count for monkey in monkeys]))[-2:]
print(two_most_active[0] * two_most_active[1])

# part 2
for i in range(len(input)): # resetting monkeys
    monkey_input = input[i]
    monkeys[i].reset_items([int(i) for i in monkey_input[1].split(': ')[1].split(', ')])
    monkeys[i].reset_inspection_count()

for i in range(10000): # this one will take a couple of seconds
    for m in range(len(monkeys)):
        monkey = monkeys[m]       
        for _ in range(len(monkey.items)):
            next_monkey, worry_level = monkey.inspect(modulo)
            monkeys[next_monkey].add_item(worry_level)
two_most_active = list(sorted([monkey.inspection_count for monkey in monkeys]))[-2:]
print(two_most_active[0] * two_most_active[1])

# Your puzzle answer was 57838
# Your puzzle answer was 15050382231
