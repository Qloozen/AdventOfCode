## Part 1

> The goal is to calculate all combinations of equations using addition and multiplication on a given list. Finally, we need to sum all test values that have an equation equal to the test value. Each line on the input has a test value and a list of numbers.

```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

### Solution

1. I used recursion to get all combinations of the operators (\* and +), based on the amount of numbers used.
2. Then I loop over the different combinations and loop over each operator. I append it to each previous result, since the operators are evaluated left to right.
3. Finally, I check if the array with results match the test value. And adding the test value to the sum.

## Part 2

> A new operator is available, which is the ||, which simply concatenates the numbers like: 1 | 5 = 15.

### Solution

My solution is not the most efficient, because I just create a bunch more combinations now... I added a new if statement to append the number instead. It takes a while for the result to print
