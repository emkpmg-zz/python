# B1 - Ask the user to enter their name and append this to a file called 'register.txt'

user_name = input("What is your name?\n")
f = open("register.txt", "w")
f.write(user_name)
