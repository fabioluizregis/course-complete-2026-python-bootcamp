friends = {
    "Rolf": 24563455,
    "Adam": 30543543,
    "Anne": 24544457
}

print(friends)

print(friends.keys())
print(friends.values())
print(friends.items())

for name, phone in friends.items():
    print(f"{name}: {phone}")