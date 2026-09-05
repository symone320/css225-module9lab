# Symone Mitchell
# September 5, 2026
# Problem 4: Numbers Divisible by 10
# This program uses a while loop to find numbers divisible by 10.

# Create an empty list
tens = []

# Start the counter at 0
counter = 0

# Continue the loop until the counter reaches 50
while counter <= 50:
    # Check if the counter is divisible by 10
    if counter % 10 == 0:
        tens.append(counter)

    # Increase the counter by 1
    counter += 1

# Display the completed list
print(tens)
