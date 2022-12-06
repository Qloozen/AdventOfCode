with open("day-06/input.txt") as f:
    input = f.read()


def find_sequence(size):
    return next(i+size for i in range(len(input)-size) if len(set(input[i:i+size])) == size)


print(find_sequence(4))
print(find_sequence(14))
