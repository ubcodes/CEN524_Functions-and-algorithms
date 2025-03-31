# Newton's Iterative Formula for Reciprocal of N
1. Input : Inital guess `x0 - 0.1`, target number `N = 5`, tolerance, and maximum iterations.
2. Loop: Until convergence or maximum iterations:
    • Compute `x_i+1 = x_i (2 - x+i N)`
    • Check for convergence if the difference between iterations is small.
3. Return: Approximate reciprocal.