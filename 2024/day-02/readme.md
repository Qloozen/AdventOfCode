## Part 1

> The goal is to check if a **report** (each line in the input) is valid. Each report contains a sequence of numbers also called **Levels**. A report is safe/valid if the levels in the report are **either all increasing or decreasing**. Also adjacent levels must **differ at least 1 and at most 3**.

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

I reworked part 1 to be reusable for part 2, therefore i created this function:

```python
def check_report(report):
    diffs = [a - b for a, b in zip(report[1:], report)]
    correct_diffs = [x != 0 and abs(x) <= 3 for x in diffs]
    decreasing_steps = list(map(lambda a: a < 0, diffs))
    return all(correct_diffs) and (all(decreasing_steps) or not any(decreasing_steps))
```

1. To check the difference between each level in the report, I zip the report with itself shifted by one. Then storing the difference of each pair. Negative differences indicate decreasing levels, vice versa.

```python
diffs = [a - b for a, b in zip(report[1:], report)]
```

2. Next I created a list of booleans, indicating if each difference is at least 1 and at most 3.

```python
correct_diffs = [x != 0 and abs(x) <= 3 for x in diffs]
```

3. To determine is a report is decreasing, I simply check if each difference is negative.

```python
decreasing_steps = list(map(lambda a: a < 0, diffs))
```

4. Finally I return if a report is safe by checking if all differences are valid and if the report is either all decreasing or increasing.

```python
return all(correct_diffs) and (all(decreasing_steps) or not any(decreasing_steps))
```

5. To get the result for part 1, run the check_report function for each report and sum up the safe reports.

```python
print(sum(check_report(report) for report in input))
```

## Part 2

> The goal of part 2 is to check if removing a single level from unsafe reports would make it safe.

To solve this, I manually loop over the reports, check if the initial check is safe or not. If not I start removing each level individually from the report and check if this makes it safe.

This is a brute forcce solution, but the reports are small enough to make this feasible.

```python
    result = 0
    for report in input:
        is_safe = check_report(report)

        if not is_safe:
            for i in range(len(report)):
                is_safe = True if check_report(report[:i] + report[i+1:]) else False
                if is_safe: break

        result += is_safe

    print(result)
```
