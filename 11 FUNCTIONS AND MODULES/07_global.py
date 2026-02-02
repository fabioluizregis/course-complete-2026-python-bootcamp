def sum(a, b):
    print("Hey, I`m summing!")
    total = a + b
    global z # declaring z as a global variable to modify it
    z = 0
    return total


z = 3
print(sum(3, 12))
print(z)