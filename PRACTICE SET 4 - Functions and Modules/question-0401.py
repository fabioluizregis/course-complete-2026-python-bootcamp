def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(3))  # Output: 6