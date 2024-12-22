with open("input.txt") as f:
    patterns, designs = f.read().split('\n\n')
    patterns = patterns.split(', ')
    designs = designs.splitlines()

    def possible(design_part, patterns):
        if len(design_part) == 0: return True

        for pattern in patterns:
            if design_part.startswith(pattern):
                if possible(design_part[len(pattern):], patterns):
                    return True

        return False        
        

    p1 = 0
    for design in designs:
        applicable_patterns = [x for x in patterns if x in design]
        p1 += possible(design, applicable_patterns)
    print(p1)

# Your puzzle answer was 342.



