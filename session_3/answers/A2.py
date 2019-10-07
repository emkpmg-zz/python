# A2 - i. Keep asking the user to enter a number until they enter the number 7, then print "Wow! Lucky number 7!
# A2 - ii. Rewrite so that the number being guessed is a random value from 1 to 10

# i
guess = None
while guess != 7:
    guess = int(input("Guess the computer's number:\n"))
print("Wow! Lucky number 7!")

# # ii
import random
guess = None
while guess != 7:
    guess = random.randint(1, 10)
    print(guess)
print("Wow! Lucky number 7!")

# iii
import random
computer_choice = random.randint(1, 10)
user_choice = 0
while computer_choice != user_choice:
    user_choice = int(input("Guess the computer's number:\n"))
    print(computer_choice)
print("Well done! You guess the computer's number!")
