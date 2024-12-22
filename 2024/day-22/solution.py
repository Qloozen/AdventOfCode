from collections import defaultdict

with open("input.txt") as f:
    intial_values = list(map(int, f.read().splitlines()))

    def get_secrets(initial_secret, n):
        mod = 16777216
        next_secrets = [initial_secret]

        for _ in range(n):
            new_secret = next_secrets[-1]
        
            new_secret ^= (new_secret * 64)
            new_secret %= mod

            new_secret ^= (new_secret // 32)
            new_secret %= mod

            new_secret ^= (new_secret*2048)
            new_secret %= mod

            next_secrets.append(new_secret)
        return next_secrets

    p1 = 0
    sequences = defaultdict(int)

    for val in intial_values:
        # part 1
        next_secrets = get_secrets(val, 2000)
        p1 += next_secrets[-1]

        # part 2
        current_sequences = defaultdict(int)
        ones = list(map(lambda x: x % 10, next_secrets))
        changes = [a - b for a, b in zip(ones[1:], ones)]
        assert(len(changes) == 2000)

        for i in range(len(changes) - 4):
            seq_key = tuple(changes[i:i+4])
            current_sequences[seq_key] = max(current_sequences[seq_key], ones[i+4])

        for k, v in current_sequences.items():
            sequences[k] += v

    print(p1)

    highest_value = 0
    for k, v in sequences.items(): 
        if v > highest_value:
            highest_value = v
            # print(k)
    print(highest_value)

    # Your puzzle answer was 13461553007.
    # 1550 too high




    
