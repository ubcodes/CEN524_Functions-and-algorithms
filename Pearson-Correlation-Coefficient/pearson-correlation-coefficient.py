import math

def pearson_correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    sum_x_sq = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_y_sq = sum((y[i] - mean_y) ** 2 for i in range(n))

    denominator = math.sqrt(sum_x_sq * sum_y_sq)

    if denominator == 0:
        return 0
    return numerator / denominator

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
print("Pearson's Correlation Coefficient:", pearson_correlation(x, y))
