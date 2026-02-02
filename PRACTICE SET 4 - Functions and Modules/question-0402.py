def sum_of_digits(n):
    """Return the sum of the digits of a non-negative integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    total = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit  # Add it to total
        n = n // 10 # Remove the last digit
    return total

print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(0))     # Output: 0
print(sum_of_digits(9999))  # Output: 36