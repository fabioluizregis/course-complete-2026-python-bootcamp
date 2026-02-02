coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

#coordinates[0] = 50  # This will raise a TypeError because tuples are immutable 
# Output: TypeError: 'tuple' object does not support item assignment

#convert tuple to list to modify
list = [list(coordinates)]
print(list)  # Output: [[10, 20]]

list[0][0] = 50
print(list)  # Output: [[50, 20]]

#Convert list back to tuple
coordinates = tuple(list[0])
print(coordinates)  # Output: (50, 20)  
