from functools import cmp_to_key

with open("input.txt") as f:
    ordering_rules, updates = f.read().split("\n\n")
    ordering_rules = [tuple(map(int, rule.split("|"))) for rule in ordering_rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    def sortFn(a, b): # for part 2
        if (a, b) in ordering_rules: return -1
        elif (b, a) in ordering_rules: return 1
        else: return 0

    
    part1, part2 = 0, 0

    for update in updates:
        is_ordered = all([update.index(x) < update.index(y) for x, y in ordering_rules if x in update and y in update])
        
        if is_ordered: # part 1
            part1 += update[len(update)//2] 
        else: # part 2
            update_sorted = sorted(update, key=cmp_to_key(sortFn))
            part2 += update_sorted[len(update_sorted)//2]


    print(part1)
    print(part2)

# Your puzzle answer was 4689
# Your puzzle answer was 6336



