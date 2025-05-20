import random
user_numbers = [] # List to store the user's numbers
count = 0 # Counter for ow many numbers match with the computer's numbers
comp_numbers = random.sample(range(1, 49), 6) # Generate 6 unique random numbers between 1 and 48 (inclusive)
# Request for six numbers
for i  in range(1, 7):
    while True:
        number = input(f"Enter {i} number: ") # Prompt the user to input a number
        try:
            number = float(number)
            if number.is_integer():
                number = int(number)
                if number in user_numbers: # Prevent duplicates
                    print("You have entered this number before!")
                    continue
                if number < 1 or number > 49: # Validate number is within allowed range
                    print("It's not in range 1-49!")
                    continue
                user_numbers.append(int(number))  # Add the valid number to the list
                break  # Exit the loop and move to the next number
            else:
                print("It's not an integer!") # Reject if not a whole number
                continue
        except ValueError:
            print("It's not a number!")
for user_number in user_numbers: # Compare the user's numbers with the computer's numbers
    if user_number in comp_numbers:
        count += 1 # Increment the match counter
# Display results
print(f"Your numbers: {sorted(user_numbers)}")
print(f"Computer numbers: {sorted(comp_numbers)}")
print(f"You have {count} numbers in common")