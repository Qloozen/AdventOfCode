with open("day-06/input.txt") as f:
    input = f.read()


def find_sequence(num):
    return next(i+num for i in range(len(input)-num-1) if len(set(input[i:i+num])) == num)


print(find_sequence(4))
print(find_sequence(14))
