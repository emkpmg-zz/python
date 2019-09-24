# D4 - Ask the user to enter a number, if the number is even, print "Even",
# otherwise print "Odd"

# Ask for user input and cast to int
number = int(input("Please enter a number: "))

# Use modulus to get the remainder, 1 is considered true and 0 false
# 1 % 2 = 1, therefor true
# 2 % 2 = 0, therefor false
# 3 % 2 = 1, therefor true
# 4 % 2 = 0, therefor false
if number % 2:
    print("Odd")
else:
    print("Even")
