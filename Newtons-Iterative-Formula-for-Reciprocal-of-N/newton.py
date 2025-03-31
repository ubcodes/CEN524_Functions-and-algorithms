def newton_reciprocal(N, x0=0.1, tolerance=1e-6, max_iter=100):
    x_i = x0
    for i in range(max_iter):
        x_next = x_i * (2 - x_i * N)
        if abs(x_next - x_i) < tolerance:
            break
        x_i = x_next
    return x_i

# Example usage
N = 5
reciprocal = newton_reciprocal(N)
print("Reciprocal of", N, "is approximately:", reciprocal)
