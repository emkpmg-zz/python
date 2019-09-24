# D1 - Ask for the user's name, if they are called "Bob", print "Welcome Bob!"

# Ask for user input
name = input("What is your name? ")

# Check to see the name is "Bob"
if name == "Bob":
    print("Welcome Bob!")

# The example above doesnt allow for users to enter "bob" or "BOB"
# So let's fix that below

# Convert the name to all lowercase before checking it
if name.lower() == 'bob':
    print("Welcome Bob!")
    
