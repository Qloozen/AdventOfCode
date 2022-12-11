ans = 0
ans2 = 0
import re
from typing import List
with open("day-11/input.txt") as f:
    input = [monkey.splitlines() for monkey in  f.read().split('\n\n')]
    # input = f.read().split("")
    # input = [int(num) for num in f.read().splitlines()]
    # input = [[int(num) for num in line] for line in f.read().splitlines()]

class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = [int(i) for i in items.split(', ')]
        self.operation = operation.split('new = ')[1]
        self.test = int(test.split('by ')[1])
        self.true = int(true.split('monkey ')[1])
        self.false = int(false.split('monkey ')[1])
        self.inspection_count = 0
    def __throw(self, worry_level) -> int:
        if (worry_level * 10) % self.test == 0:
            # print('     Current worry level is divisible by '+ str(self.test))
            return self.true
        else:
            # print('     Current worry level is divisible by '+ str(self.test))
            return self.false

        # return self.true if worry_level % self.test == 0 else self.false

    def inspect(self, round):
        self.inspection_count += 1
        item = self.items.pop(0)
        # print(' Monkey inspects an item with a worry level of ' + str(item))
        evaluation = self.get_eval(item)
        worry_level = eval(evaluation)
        # print('     Worry level = ' + evaluation + ' = ' + str(worry_level))
        worry_level //= 3
        # print('     Monkey gets bored with item. Worry level is divided by 3 to ' + str(worry_level))
        next_monkey = self.__throw(worry_level)
        # print("     Item with worry level " + str(worry_level) +  ' is thrown to monkey ' + str(next_monkey))
        return (next_monkey, worry_level)

    def get_eval(self, worry_level):
        return self.operation.replace('old', str(worry_level))

    def add_item(self, item):
        self.items.append(item)
    def __str__(self) -> str:
        return ', '.join(str(x) for x in self.items)



monkeys: List[Monkey] = []
for monkey_input in input:
    items = monkey_input[1].strip().split('Starting items: ')[1]
    operation = monkey_input[2].strip().split('Operation: ')[1]
    test = monkey_input[3].strip().split('Test: ')[1]
    true = monkey_input[4].strip().split('If true: ')[1]
    false = monkey_input[5].strip().split('If false: ')[1]
    monkey = Monkey(items, operation, test, true, false)
    monkeys.append(monkey) 

for i in range(20):
    for m in range(len(monkeys)):
        monkey = monkeys[m]       
        # print("Monkey " + str(m))
        for _ in range(len(monkey.items)):
            next_monkey, worry_level = monkey.inspect(i)
            monkeys[next_monkey].add_item(worry_level)
    print("After round: " + str(i + 1))
    for m in range(len(monkeys)):
        monkey = monkeys[m]       
        # print("Monkey " + str(m) + ': ' + monkey.__str__())
        print("Monkey " + str(m) + ' inspected items ' + str(monkey.inspection_count) + ' times.')


two_most_active = list(sorted([monkey.inspection_count for monkey in monkeys]))[-2:]

print(two_most_active[0] * two_most_active[1])
print(ans2)