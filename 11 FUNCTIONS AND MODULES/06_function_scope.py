def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1  # z is also a local variable
    return c

z = 8
print(sum(7, 3))
print(z)  # z is a global variable