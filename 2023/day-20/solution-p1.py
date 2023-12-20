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

    for part in parts.splitlines():
        values = part[1:-1].split(",")
        part_map = {category: int(rating) for category, rating in (value.split("=") for value in values)}
        all_parts.append(part_map)


accepted, rejected = [], []

for parts in all_parts:
    print("PART:" + str(parts))
    workflow = 'in'
    finding = True
    while finding:
        print(workflow)
        conditions = workflow_map[workflow]
        for condition in conditions:
            if len(condition) == 1:
                if condition[0] == "R": 
                    rejected.append(parts)
                    finding = False
                    break
                elif condition[0] == "A": 
                    accepted.append(parts)
                    finding = False
                    break
                else: 
                    workflow = condition[0]
                    break
            else:
                category, operator, value, _, destination = condition
                larger = operator == ">" and parts[category] > int(value)
                smaller = operator == "<" and parts[category] < int(value)
                if larger or smaller:
                  if destination == "R": 
                      rejected.append(parts)
                      finding = False
                      break
                  elif destination == "A": 
                      accepted.append(parts)
                      finding = False
                      break
                  else: 
                      workflow = destination
                      break
                    

total_accepted = 0
for parts in accepted:    
    for rating in parts.values():
        total_accepted += rating   

print(total_accepted)

#Your puzzle answer was 368523.    