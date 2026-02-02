def increment():
    global counter
    counter += 1
    return counter

counter = 0
print(increment())  # Output: 1
print(increment())  # Output: 2
print(increment())  # Output: 3