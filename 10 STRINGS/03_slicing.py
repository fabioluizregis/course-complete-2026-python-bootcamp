name = "Fabio"

print(name[0])    # F

print(name[0:2])
print(name[2:-1])   # same as name[2:4]
print()

name2 = "Fabio231234u234879dwh89"
print(name2[0:10])
print(name2[0:10:1])   # same as name2[0:10]
print(name2[0:10:2])   # skip every second character
print(name2[0:10:3])   # skip every third character

print()
print(name2[:4])    # same as name2[0:4]
print(name2[1:])    # same as name2[1:len(name2)]
