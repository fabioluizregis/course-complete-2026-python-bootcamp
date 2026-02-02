marks = {'Math': 95, 'Science': 88, 'English': 92}

print(marks.keys())    # Output: dict_keys(['Math', 'Science', 'English'])  
print(marks.values())  # Output: dict_values([95, 88, 92])

print(marks.items())   # Output: dict_items([('Math', 95), ('Science', 88), ('English', 92)])   

# Using items() to iterate through key-value pairs
for subject, score in marks.items():
    print(f"{subject}: {score}")

marks.pop('Science')  # Removes 'Science' and returns its value
print(marks)

marks.clear()         # Removes all items from the dictionary
print(marks)          # Output: {}