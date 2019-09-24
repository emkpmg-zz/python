# D5 - Ask the user for 2 different numbers, if the total of the two numbers
# is over 21, print "Bust" otherwise print "Safe"

# Ask for user input and cast to integers
number_1 = int(input("Please enter your first number: "))
number_2 = int(input("Please enter your second number: "))

# Work out the total of the 2 numbers
total = number_1 + number_2

if total > 21:
    # Total is greater than 21
    print("Bust")
else:
    # Total is less than or equal to 21
    print("Safe")

# Test with:
# 10, 1 = safe
# 30, 1 = bust
# 21, 0 = safe
# 21, 1 = bust
# 0, 0 = safe 
# -1, -1 = safe
