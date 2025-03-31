# Taylor Series Summation Algorithm
1. Input: Array of derivatives `[f(a), f'(a), ..., f^n(a)]`, value of `a`, value of `x`, and number of terms `n`.
2. Initialize: `sum = 0`
3. Loop: For  `i` from `0` to `n`:
    • Calculate term using the formula:
        ```python
        term = f^i(a) * (x - a)^i/i!
        ```
    • Add term to `sum`
4. Return : The summation result.