a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)
print(c)  # Output: {1, 2, 3, 4, 23, 55}

d = a.intersection(b)
print(d)  # Output: {1, 23} 

e = a.difference(b)
print(e)  # Output: {3}

