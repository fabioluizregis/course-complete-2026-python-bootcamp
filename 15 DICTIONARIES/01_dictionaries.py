marks = {'Math': 95, 'Science': 88, 'English': 92}

print(marks)
print(type(marks))

# Accessing values
print(marks['Math'])        # Output: 95
print(marks.get('Science')) # Output: 88

# Adding a new key-value pair
marks['History'] = 90
print(marks)

# Updating an existing value
marks['English'] = 94
print(marks)

# Removing a key-value pair
del marks['Science']
print(marks)

