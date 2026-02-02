def add(a, b, plus=0):
    """Returns the sum of a and b, plus an optional value."""
    return a + b + plus

result1 = add(5, 10)
print("Result without optional argument:", result1)

result2 = add(5, 10, 3)
print("Result with optional argument:", result2)

result3 = add(b=7, a=2)
print("Result with keyword arguments:", result3)