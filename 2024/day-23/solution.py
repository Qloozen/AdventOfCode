from collections import defaultdict

with open("input.txt") as f:
    network = defaultdict(list)

    for line in f.read().splitlines():
        a, b = line.split('-')
        network[a].append(b)
        network[b].append(a)


    threepairs = set()
    for a, conn_a in network.items():
        for b in conn_a:
            for c in network[b]:
                if c == a: continue
                conn_c = network[c]

                if a in conn_c:
                    pair = tuple(sorted((a, b, c)))
                    if a.startswith('t') or b.startswith('t') or c.startswith('t'): 
                        threepairs.add(pair)

    print(len(threepairs))

    # part 2
    largest_network = {}

    for computer, connections in network.items():
        lan = {computer}

        for other in connections:
            if all(other in network[pc] for pc in lan):
                lan.add(other)
        if len(lan) > len(largest_network):
            largest_network = lan

    print(','.join(sorted(largest_network)))

# Your puzzle answer was 1358.
# Your puzzle answer was cl,ei,fd,hc,ib,kq,kv,ky,rv,vf,wk,yx,zf.


