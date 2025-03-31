import math

def taylor_series_sum(derivatives, a, x, n):
    total_sum = 0
    for i in range(n):
        term = (derivatives[i] * ((x - a) ** i)) / math.factorial(i)
        total_sum += term
    return total_sum

# Example usage
derivatives = [1, 2, 4, 6]  # Example derivatives f(a), f'(a), f''(a), ...
a = 1
x = 2
n = len(derivatives)
result = taylor_series_sum(derivatives, a, x, n)
print("Taylor Series Sum:", result)
