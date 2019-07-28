if True:
    print("This is always run")

if False:
    print("This is never run")


age = 21
if age > 18:
    print("You are older than 18")

if age >= 18:
    print("You are 18 or older")

if age < 18:
    print("You are younger than 18")

if age == 18:
    print("You are 18")

if age != 21:
    print("You're not 21")


# Ask for the users name and convert it to lowercase
name = input("What's your name? ").lower()
if name == "alice":
    print("Hey Alice!")

if name != "alice":
    print("You're not Alice")
