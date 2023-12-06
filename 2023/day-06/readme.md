## Part 1

**Short summary of the context:**

Given the following input, there are 3 races with a time value and a distance value:

```
Time:      7  15   30
Distance:  9  40  200
```

The **time** value is how long you may move + charge the boat. Lets say time: 7, charge for 2 & move for 5. Charging determines how fast you can move. In this context the charge duration == speed. So charging for 2 & move for 5 means 2 \* 5 = 10 distance. You can't charge + move at the same time, and you can only charge once.

The **Distance** value is the current distance record with the corresponding race time. The goal is to find all the possible ways to beat the current record. So for the race (time: 7, 'record': 9). charge for 2 \* move for 5 = 10. So this is a possible way to win.

**Approach:**

I created a simple function that returns the possible amount of ways to win per game. The function kinda brute forces all the possible ways, by trying all the possible combinations of charging and moving:

```python
def find_possible_records(max_time, record):
  possible_records = 0
  for hold in range(0, max_time+1):
    distance = hold * (max_time - hold)
    possible_records += distance > record
  return possible_records
```

Then I perform this function for each game and get the product of all possible ways:

```python
records_per_game = [find_possible_records(max_time, record) for max_time, record in races]
print(math.prod(records_per_game))
```

Pretty simple... but it works!

## Part 2

Just a minor change of the context. The input is now only 1 game in stead of multiple games:

```
Time:      71530
Distance:  940200
```

With my approach in part 1, I just tried to use the same function and see if it works. It did, but it took around 7 seconds to find the possible ways.

**Optimization time:**

Although I already had working code, I had the urge to find a better way. So if you look at how you actually brute force it you might see something like this for a single game (remember carge time + moving time == total time):

<table>
  <tr>
    <th>Carge time:</th>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
  <tr>
    <th>Moving time:</th>
    <td>7</td>
    <td>6</td>
    <td>5</td>
    <td>4</td>
    <td>3</td>
    <td>2</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <th>Distance:</th>
    <td>0</td>
    <td>6</td>
    <td><b>10</b></td>
    <td><b>12</b></td>
    <td><b>12</b></td>
    <td><b>10</b></td>
    <td>6</td>
    <td>0</td>
  </tr>
</table>

As you can see in above table, if you know the first combination of charge time and moving time, you can easily calculate the range of winning races. In this case you start winning at a combination (charge: 2, move: 5) = 10 so that means the last combination will be the reverse (charge: 5, move: 2) = 10. Calculate how many numbers are between this range, including these combinations.

Now you basically have the answer at the moment you find the first combination that wins.

Changed function:

```python
def find_possible_records(max_time, record):
  for hold in range(0, max_time+1):
    distance = hold * (max_time - hold)
    if distance > record:
      range_end = max_time - hold
      range_length = (range_end - hold) + 1
      return range_length
```
