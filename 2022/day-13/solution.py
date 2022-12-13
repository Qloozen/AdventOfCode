ans = 0
with open("day-13/input.txt") as f:
    input = [[eval(packet) for packet in pair.splitlines()] for pair in f.read().split('\n\n')]
with open("day-13/input.txt") as f:
    input2 = [eval(packet) for packet in f.read().replace('\n\n', '\n').splitlines()]
    divider_a, divider_b = [[2]], [[6]]
    input2.extend([divider_a, divider_b]) 


def compare_lists(a, b):
    compare = zip(a, b)
    for left, right in compare:
        if type(left) == list or type(right) == list:
            next_a = [left] if type(left) == int else left
            next_b = [right] if type(right) == int else right
            res = compare_lists(next_a, next_b)
            if res == None: continue
            return res
        else:
            if left < right :
                return True
            if right < left :
                return False
    if len(a) == len(b):
        return None 
    return len(a) < len(b)


# part 1
for i in range(len(input)):
    is_valid = compare_lists(input[i][0], input[i][1])
    if is_valid: ans += i+1
print(ans)

# part 2
def bubble_sort(unordered_list) -> bool:
    all_sorted = True
    for i in range(len(unordered_list)-1):
        is_valid = compare_lists(unordered_list[i], unordered_list[i+1])
        if not is_valid:
            unordered_list[i], unordered_list[i+1] = unordered_list[i+1], unordered_list[i]
            all_sorted = False
    return all_sorted

unordered_list = input2
needs_sorting = True
while needs_sorting:
    needs_sorting = not bubble_sort(unordered_list)

print((unordered_list.index(divider_a)+1) * (unordered_list.index(divider_b) + 1))