with open("input.txt") as f:
    # Part 1
    l, r = map(list, zip(*(map(int, line.split()) for line in f.read().splitlines())))
    ans1 = sum(abs(r-l) for l, r in zip(sorted(l), sorted(r)))
    print(ans1)

    # Part 2
    sim = list(set(l) & set(r))
    ans2 = sum(i * r.count(i) * l.count(i) for i in sim)

    print(ans2)


# Your puzzle answer was 1765812
# Your puzzle answer was 20520794



