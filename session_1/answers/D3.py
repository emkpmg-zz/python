# D3. Ask the user for a password, if they enter the password "qwerty123",
# print "You have successfully logged in". If they get it wrong,
# print "Password failure"

# Ask for user input
password = input("Please enter your password: ")

# Passwords are usualy case sensitive so dont change the users input
if password == "qwerty123":
    # The password entered was correct
    print("You have successfully logged in")
else:
    # The password entered was wrong
    print("Password failure")
