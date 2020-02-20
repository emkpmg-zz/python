#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:39:44 2020

@author: dakuoko
"""
        ################################################################  .SECTION A.  ################################################################

#Q1 Write a function that prints your name

print('ama')

#Q2 Write a function that accepts a name as a parameter and prints "Hello, "

def nam(name):
    print('Hello ' + name)
    


#Q3 Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote
listNames = ["Alice", "Bob", "Charlie"]
for i in listNames:
    nam(i)



#WQ4 rite a function that prints the area of two passed in parameters
def area(p1, p2):
    print(p1*p2)
    
    
#Q5 Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list
def print_list(list_var):
    for i in list_var:
        print(i)
    
    
    
    
#Q6 Put the following into a function:
#If they are younger than 11, print "You're too young to go to this school"
#If they are between 11 and 16, print "You can can come to this school"
#If they are over 16, print 'You're too old for school"
#If they are 0, print "You're not born yet!"
        
def fnc():
    age = input('enter your age')
    if age < 11:
        print('you are too young')
    elif age >=11 and  age<= 16:
        print('you are too young for school')
    elif age > 16:
        print('you are too old for school')
    elif age == 0:
        print('you are not born yet')
    else:
        print('your age is not within specified conditions. Musy be 0 or more')
        



        ################################################################  .SECTION B.  ################################################################
        
      #EXAMPLE OF A RECURSIVE FUNCTION  
def calc(x):
    if x == 1:
        return 1
    else:
        return(x * calc(x-1))
        
        
        #calling function example
calc(7)       





#Q1 Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (
##hint: x % 2 will return true for all odd numbers)

def is_odd(x):
    if x%2 == 0:
        print(x, ' is even')
        return False
    else:
        print(x, ' is odd')
        return True
    
    
        #calling function example
is_odd(7)


#Q2 Write a function that accepts a string / word and returns it backwards, e.g. 'hello' -> 'olleh
def accept(word):
    for i in range(len(word)):
        print(word[((len(word)-1)-i)])

        #calling function example
accept('print me in reverse')
    




#Q3 Write a recursive function that accepts a number and prints that number of stars, 
#followed by ever decreasing stars on each line
def rec(num):
    print('•' * num)
    lowest = 1
    if num > lowest:
        rec(num-1)
        
        #calling function example
rec(10)





#Q3 Write a recursive function that accepts a number and prints that number of stars, 
#followed by ever increasing stars on each line
def rec(num):
    print('•' * num)
    highest = 100
    if num < highest:
        rec(num+1)
        
        #calling function example
rec(10)




#Q4 Create a padlock function. You need to be able to pass in a passcode and if its correct it should return 
#"Unlock", else "Locked" 
def padlock(passcode):
    correctCode = 'yea22##'
    if passcode == correctCode:
        return "unlock"
    else:
        return "Locked"

        #calling function example
padlock('yea22#')      #this must return locked   
padlock('yea22##')      #this must return unlock      

    
    
    
#Q5. Write a function that returns the sum of multiples of 3 and 5 between 0 and 
#limit (parameter). For example, if limit is 20, it should return the sum 
#of 3, 5, 6, 9, 10, 12, 15, 18, 20 ≈
def mult3(limit_param):
    lowest = 0
    sumMulties = 0
    multies = 0
    if limit_param < lowest:
        print('limit param must be more than 0')
    else:
        for i in range(limit_param):
            multies = i*3
            if multies >= limit_param:
                break
            else:
                print(multies)
                sumMulties += multies
            
    print('sum of multiplles of three between 0 and ', limit_param, ' is ', sumMulties)


        #calling function example
mult3(20)

   


  
#Q6. Write a function called is_prime() that accepts a number and 
#return True or False if the number of prime or not  
def is_prime(num):
    for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
       else:
           print(num,"is a prime number")

        #calling function example
is_prime(99)
    
    
    
    
    
            ################################################################  .SECTION C.  ################################################################

    
#Q1. Read the file 'jabberwocky.txt' and print its content to the screen
#Q2. Ask the user to enter their name and append this to a file called 'register.txt'
#Q3. Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file
#Q4. Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'
#Q5. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. Work out what the secret message says
#Q6. Benford’s law states that the leading digits in a collection of data are probably going to be small. For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. Work out which of the files contains fake data.
    
    
    
    
        
