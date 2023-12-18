## Part 1

This problem kind of looked like the puzzle of day-10. Firstly I tried calculating the distance between each point on each row, but it was very optimistic to think the loop would not cross multiple times on a row. So I used an algorithmn that some people suggested for day-10 called the Shoelace algorithm. Defined as:
$$\frac{1}{2}|\sum^{n-1}_{i=1} x_i y_{i+1} + x_n y_1 - \sum^{n-1}_{i=1} x_{i + 1}y_i - x_1 y_n|$$

Which is done in these steps:

1. for each coordinate pair (x, y) in the polygon, multiply **x** by the **y-value** of the next coordinate pair in the polygon. The last coordinate pair is multiplied by the y-value of the first coordinate pair. Get the sum of these products.
2. for each coordinate pair (x, y) in the polygon, multiply **y** by the **x-value** of the next coordinate pair in the polygon. The last coordinate pair is multiplied by the x-value of the first coordinate pair. Get the sum of these products.
3. Get the absolute value of the difference between the results from steps 1 and 2. Divide this number by 2.

To calculate the entire area we can use Pick's theorem.

From wikipedia:
$$A = i + \frac{b}{2} - 1$$
A= is the polygon area
i= is the number of interior points
b= is the number of boundary points

We have the area calculated with the Shoelace algorithm, we need to calculate the number of interior points and the number of boundary points.

$$i = A - \frac{b}{2} + 1$$

The boundary points are calculated by just counting the length of the steps while parsing the input.

Add the interior points to the boundary points and we have the solution.

## Part 2

We can leave part 1 as it is and just change how we format the input. And its done
