with open("input.txt") as f:
    input = [list(map(int, line.split())) for line in f.read().splitlines()]

    def check_report(report): 
        diffs = [a - b for a, b in zip(report[1:], report)]
        correct_diffs = [x != 0 and abs(x) <= 3 for x in diffs]
        decreasing_steps = list(map(lambda a: a < 0, diffs))
        return all(correct_diffs) and (all(decreasing_steps) or not any(decreasing_steps))
    
    # part 1
    print(sum(check_report(report) for report in input))

    # part 2 - brute force :-(
    result = 0
    for report in input:
        is_safe = check_report(report)

        if not is_safe: 
            for i in range(len(report)):
                is_safe = True if check_report(report[:i] + report[i+1:]) else False
                if is_safe: break
        
        result += is_safe
        
    print(result)

    # Your puzzle answer was 442
    # Your puzzle answer was 493
