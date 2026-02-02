word = "hello world"

print(word)
print(len(word))
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())
print()

word2 = "    hello world    "
print(word2)
print(word2.strip())
print(word2.lstrip())
print(word2.rstrip())
print()

text = "Python is fun. I love Python."
print(text)
print(text.find("is"))
print(text.replace("fun", "awesome"))
print()

fruits = "apple, banana, cherry"
print(fruits.split(","))
print(",".join(["apple", "banana", "cherry"]))
print()

text = "Python123"
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.startswith("Py"))
print(text.endswith("123"))
print(text.isspace())