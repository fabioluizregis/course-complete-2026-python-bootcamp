# String formating

template = "Dear {}, your balance is {} USD."

a = "John"
a1 = 230.2346

b = "Jane"
b1 = 1200.5

c = "Doe"
c1 = 3400.4567

s1 = template.format(a, round(a1, 2))

print(s1)

print(f"Dear {b}, your balance is {round(b1, 2)} USD.")