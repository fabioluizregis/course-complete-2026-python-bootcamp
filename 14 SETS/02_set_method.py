s = {34, 23, 1, 3, 22}

print(s)

s.add(99)
s.add(1001)
print(s)


s.remove(3)
print(s)
# s.remove(2342354)   # KeyError: 2342354
s.discard(2342354)  # No error
print(s)
