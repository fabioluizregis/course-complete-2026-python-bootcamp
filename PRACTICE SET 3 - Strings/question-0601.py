sentence = input("Enter a sentence: ")
sum = 0
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for char in sentence:
    if char in vowels:
        sum += 1

print("Number of vowels:", sum)