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
ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

def get_product(ranges):
    amounts = [(end - start) + 1 for start, end in ranges.values()]
    return math.prod(amounts)

def calculate_combinations(name, ranges):
    if name == 'A': return get_product(ranges)
    elif name == "R": return 0

    total = 0
    workflow = workflow_map[name]
    for condition in workflow:
        if len(condition) == 1: total += calculate_combinations(condition[0], ranges)
        else:
            category, operator, rating, _, destination = condition
            rating = int(rating)
            range_start, range_end = ranges[category]

            if operator == '>':
                if range_start > rating < range_end:
                    containing_range: (range_start, range_end)
                    next_ranges = ranges.copy()
                    next_ranges[category] = containing_range
                    total += calculate_combinations(destination, next_ranges)
                    break # range falls completely in the next workflow, so ignore the rest
                elif range_end > rating >= range_start:
                    containing_range = (rating+1, range_end)
                    rest = (range_start, rating)
                    next_ranges = ranges.copy()
                    next_ranges[category] = containing_range
                    total += calculate_combinations(destination, next_ranges)# range falls partially in the next workflow
                    ranges[category] = rest  #the rest will be evaluated in this workflow
            if operator == '<':
                if range_start < rating > range_end:
                    containing_range: (range_start, range_end)
                    next_ranges = ranges.copy()
                    next_ranges[category] = containing_range
                    total += calculate_combinations(destination, next_ranges)
                    break # range falls completely in the next workflow, so ignore the rest
                elif range_end >= rating > range_start:
                    containing_range = (range_start, rating-1)
                    rest = (rating, range_end)
                    next_ranges = ranges.copy()
                    next_ranges[category] = containing_range
                    total += calculate_combinations(destination, next_ranges)# range falls partially in the next workflow
                    ranges[category] = rest  #the rest will be evaluated in this workflow

    return total                

print(calculate_combinations('in', ranges))

# Your puzzle answer was 124167549767307.

 