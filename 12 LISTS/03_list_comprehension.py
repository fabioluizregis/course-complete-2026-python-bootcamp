# Create a list containing the table of 5

a = 5
res = []

for i in range(1, 11):
    multiplication = a * i
    str = (f"{a} x {i} = {multiplication}")
    res.append(str)

print(res)