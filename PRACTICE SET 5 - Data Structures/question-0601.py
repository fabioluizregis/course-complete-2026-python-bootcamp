numbers = []

constinue_adding = True
while constinue_adding:
    user_input = input("Enter a number to add to the list (or type 'stop' to finish): ")
    if user_input.lower() == 'stop':
        constinue_adding = False
    else:
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")  

print(numbers)

not_duplicate_numbers = set(numbers)
print(not_duplicate_numbers)
