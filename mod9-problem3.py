# Symone Mitchell
# September 5, 2026
# Problem 3: Number List and Sum
# This program asks the user to enter numbers until their total is greater than 100.

# Create an empty list to store the numbers
numbers = []

# Start the total at 0
total = 0

# Continue asking for numbers while the total is 100 or less
while total <= 100:
    number = int(input("Enter a number: "))
    numbers.append(number)
    total = sum(numbers)

# Display the numbers entered and their total
print("Numbers entered:", numbers)
print("Total:", total)
