## Part 1

> The input is a list of computer in pairs of two. The goal is to find sets of three inter-connected computers and filter out the sets where none of the computers starts with 't'

### Approach

I started of by creating a dictionary with all the computers and their connections. For each PC I check 3 deep into their connections. If the connection in the 3rd level also has a connection to the original PC, we then know that we have a set of 3 inter-connected computers.

I then store this group of 3 computers as tuple in a global set. I sort this tuple to prevent adding the same group with different orders.

Before storing the group, I check if any of the computers start with 't'.

## Part 2

> The goal is to find the largest lan group in the input data. So the largest set of computers that are all connected to each other. Then we need to sort the computers by name and return it as a string.

### Approach

For each PC I construct a potential network. I start with the current PC alone in the network. Then I loop over all of its connections and add the connection if that connection is connected to the whole network.

After I checked every connection of a computer, I overwrite the current largest network with this one.
