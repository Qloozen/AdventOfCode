## Part 1

> The input contains grids, which are either locks or keys. Locks are read top to bottom, so the top row is filled with `#`. Keys are read bottom to top, bottom row is all `#`. The columns of a grid are the heights of the locks/keys. The goal is to find the keys that fit in a lock. A key fits in a lock if the heights of the keys are less or equal to the total available height (aka if the key pins overlap the lock pins, it doesn't fit).

### Approach

Pretty straightforward, just convert the locks and keys to a list of numbers (heights of the pins). Then compare each key with each lock to see if it fits. The sum of a and b should not exceed R-2. -2 because we don't include the top of the locks and the bottom of the keys.

## Part 2

**Part 2 is locked for me, because I do not have enough stars yet**
