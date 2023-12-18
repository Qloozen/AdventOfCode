## Part 1

To solve part 1 I used the dijkstra algorithm to find a path with a minimun heat loss, with maximum 3 steps in the same direction. To do this I followed a basic example that uses a priority queue: https://builtin.com/software-engineering-perspectives/dijkstras-algorithm. I also created a Node class that also holds the steps it took in a certain direction. This was a bad idea since the steps were shared referenced by different directions.To fix this I converted my class to a namedtuple, and this worked.

So from the start I move in every possible direction, set the step to 1, saved the direction it went, and added it to the priority queue. After that I repeat the process, but for noded going in the same direction I add 1 to the current amount of steps, in that direction. Once I reach a node that exceeds the maximum amount of steps I skip that direction.

## Part 2

So for part 2 it is much nicer to separate the if statements for going in the same direction and going to different directions. So now with a minimum of 4 steps in the same direction, and a maximum of 10 steps. Every 4th step in the same direction I go every other direction, while also keep going in the same direction till 10 steps.
