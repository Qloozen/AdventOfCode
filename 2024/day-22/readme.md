## Part 1

> The input is a list with inital numbers (secret numbers). Based on some simple calculations on the number, we can calculate the next 'random' secret. For each secret number in the input list, we need to calculate the 2000th secret number and sum them up (excluding the inital secret number).

### Approach

I created a function that takes in a secret number and performs the given calculations 2000 times. It will return a list of all the secret numbers, including the inital secret number. The reason I return a list instead of a single value (2000th secret number) is because we need the whole list for part 2.

To get the total sum, call this function for each secret number in the input list and access the last value in the list.

## Part 2

> For each secret number in the input list (aka buyers), we have the next 2000 secret numbers. From these numbers, the ones digit is the actual price. The monkeys only sell based on the price changes between the secret numbers, specifically at sequences of 4 consecutive changes. For example after sequence of changes: (-1, -1, 0, 2) the price is 7. The goal is to get the largest price per buyer, but we can only use one sequence for all buyers. So eg. sequence (-1, -1, 0, 2) for buyer A = 7, buyer B = 4, buyer C = does not have this sequence, is in total 11.

### Approach WIP

My approach is to first convert the list of secret numbers per buyer to a list of prices (ones digits). This is done with `secret % 10`, or alternatively you can convert the secret number to a string an get the last character. So per buyer I have something like this [2,5,7,9,2,1,0,2].

Next up determine the subsequent changes. I zip the list with itself, shitfted with 1. Resulting in a list of changes. Eg [3,2,2,-7,-1,-1,2].

Next up is to iterate this list of changes by 4. Checking each iteration what the price is after 4 changes. Eg after (3, 2, 2, -7) the price is 2. I keep track of the highest price in a dictionary, with the sequence as key and the price as value.

I also have a global dictionary that stores these values for all buyers. For each sequence I just add up the values per buyer.

Finally I loop over the global dictionary and return the highest price.

_NB: My assumption was that if a sequence of 4 appear more than once, in the same price list. The higest price of that sequence is used. Not entirely sure why this is not the case. But when I say my answer was too high I tried adding a set of seen sequences, and ignored duplicate sequences_
