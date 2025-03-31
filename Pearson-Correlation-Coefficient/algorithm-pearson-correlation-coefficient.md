# Pearson's Correlation Coefficent Algorithm
1. Input Arrays `x` and `y` of length `n`
2. Compute: Means of `x` and `y` , denoted as `mean_x` and `mean_y`
3. Initialize: `numerator = 0`, `sum_x_sq = 0`, `sum_y_sq = 0`
4. Loop : For `i` in range `n`:
    • Update `numerator += (x[i] - mean_x) * (y[i] = mean_y)`
    • Update `sum_x_sq += (x[i] - mean_x) ** 2`
    • Update `sum_y_sq += (y[i] - mean_y) ** 2`
5. Compute: Correlation `r`
```python
r = numerator/ (√sum_x_sq * sum_y_sq)
```
6. Return `r`