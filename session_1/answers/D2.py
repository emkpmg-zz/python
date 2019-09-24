# D2 - Ask for the user's name, if they are not called "Alice",
# print "You're not Alice!"

# Ask for user input
name = input("What is your name? ")

# Convert the name to all lowercase before checking it
if name.lower() != "alice":
    print("You're not Alice!")
