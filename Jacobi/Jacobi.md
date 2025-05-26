

## Extended Jacobi Iteration

In the previous Jacobi example, the data at the matrix boundaries were unchanged, meaning only the internal data points were updated iteratively:
b(i,j) = 0.25 * [a(i+1,j) + a(i-1,j) + a(i,j+1) + a(i,j-1)], where 1 < i, j < N (N represents the matrix dimension)

Now, data updates are also required at the boundary points:
b(i,j) = 0.25 * [a(i+1,j) + a(i-1,j) + a(i,j+1) + a(i,j-1)], where 1 ≤ i, j ≤ N

The condition is that the entire matrix is periodically wrapped, for example, for the update of a(1,1) it is like this:
b(1,1) = 0.25 * [a(2,1) + a(N,1) + a(1,2) + a(1,N)]

Tips:
- Add appropriate conditional judgments to handle boundary points
- Complete the serial program first, then try parallel programming
- The first iteration's leftmost column and the last iteration's rightmost column are both useful