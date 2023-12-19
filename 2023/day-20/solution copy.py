import re 
with open("input.txt") as f:
    workflow_map = {}
    all_parts = []

    workflows, parts = f.read().split("\n\n") 
    for workflow in workflows.splitlines():
        name = workflow[:workflow.index("{")]
        conditions = workflow[workflow.index("{") + 1:workflow.index("}")].split(",")
        conditions = [re.split(r'(>|<|:)', condition) for condition in conditions]
        workflow_map[name] = conditions



import math

idx = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def get_combinations(workflow, ranges):
    conditions = workflow_map[workflow]
    total = 0
    # print("WORKFLOW: " + workflow + " - Input ranges: " + str(ranges))
    for condition in conditions:
        if len (condition) == 1:
            if condition[0] == "R": break
            elif condition[0] == "A": 
                product = math.prod([(end - start) + 1 for start, end in ranges])
                total += product
                print("product: " + str(product) + " from: " + str(ranges)) 
            else: 
                # print(str(condition) + " Input range: " + str(ranges))
                total += get_combinations(condition[0], ranges.copy())
        else:
            category, operator, value, _, destination = condition
            # print(category + operator + value + _, destination + " Input range: " + str(ranges))
            value = int(value)

            start, end = ranges[idx[category]]
            if operator == "<" and start < value:
                next_ranges = ranges.copy()
                next_ranges[idx[category]] = (start, min(value-1, end))
                if destination == "R": break
                elif destination == "A": 
                    product = math.prod([(end - start) + 1 for start, end in next_ranges])
                    total += product
                    print("product: " + str(product) + " from: " + str(next_ranges)) 
                else: total += get_combinations(destination, next_ranges)
                ranges[idx[category]] = (value, end)
            
            elif operator == ">" and end > value:
                next_ranges = ranges.copy()
                next_ranges[idx[category]] = (max(value+1, start), end)
                if destination == "R": break
                elif destination == "A": 
                    product = math.prod([(end - start) + 1 for start, end in next_ranges])
                    total += product
                    print("product: " + str(product) + " from: " + str(next_ranges)) 
                else: total += get_combinations(destination, next_ranges)
                ranges[idx[category]] = (start, value)
                
    return total
print(get_combinations("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])*3)
# 129195