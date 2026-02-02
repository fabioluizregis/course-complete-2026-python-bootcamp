num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print("Reversed number:", reversed_num)


''''
This works by:

Taking the last digit with num % 10
Adding it to reversed_num after shifting existing digits left
Removing the last digit with integer division num // 10
Repeating until num becomes 0
'''