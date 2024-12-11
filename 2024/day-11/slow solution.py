# Part 2 will not run with this solution !!

with open("input.txt") as f:
    input = list(map(int, f.read().split()))

    for _ in range(25):
        i = 0 
        while i < len(input):  
            s = str(input[i])

            if input[i] == 0: input[i] = 1
            elif len(s) % 2 == 0: 
                l, r = s[:len(s)//2], s[len(s)//2:]
                input[i] = int(r)
                input.insert(i, int(l))
                i+=1
            else:
                input[i] *= 2024
            i+=1
    print(len(input))

