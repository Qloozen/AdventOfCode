# part 1
with open("input.txt") as f:
    input = f.read()

    disk_map = []
    id_index = 0
    for i, num in enumerate(input):
        if i % 2 == 0: 
            disk_map += [str(id_index)] * int(num)
            id_index+=1
        else: disk_map += ['.'] * int(num)

    for i in range(len(disk_map)-1, -1, -1):
        first_space = disk_map.index(".")
        if first_space > i: break

        disk_map[first_space] = disk_map[i]
        disk_map[i] = "."


    total = 0
    for i, id in enumerate(disk_map):
        if id == '.': break
        total += i * int(id)
    print(total)


# part 2
with open("input.txt") as f:
    input = f.read()

    disk_map = []
    last_id = 0
    for i, num in enumerate(input):
        if i % 2 == 0: 
            disk_map.append((last_id, int(num)))
            last_id += i < len(input) - 2                       
        elif num != '0': disk_map.append((".", int(num)))

    while last_id != 0:
        target_index, target = [(i, x) for i, x in enumerate(disk_map) if x[0] == last_id][0]
        target_el, target_amount = target

        for i in range(len(disk_map)):
            el, space = disk_map[i]
            if i > target_index: break
            if el == "." :
                if target_amount == space: 
                    disk_map[target_index] = (".", target_amount)
                    disk_map[i] = target
                    break
                elif target_amount < space:
                    left_over = space - target_amount
                    
                    disk_map[i] = (".", left_over)
                    disk_map[target_index] = (".", target_amount)
                    disk_map.insert(i, target)
                    break
        last_id -= 1
                
    input = 0
    
total = 0
pos = 0
for el, amount in disk_map:
    for _ in range(amount):
        if el != ".": total += el * pos
        pos += 1
print(total)

# Your puzzle answer was 6370402949053.
# Your puzzle answer was 6398096697992.