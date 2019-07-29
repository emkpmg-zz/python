# [fit] IHF: Code
## Python — Session 2

---

# Review

---

# Running a Python Script

---

# Running a Python Script

```
$ python <file_name>.py
```

---

# Variables

---

# Variables

```python
name = "Charlie"
age = 27
left_to_pay = 29.99
has_paid = False
```

---

# Data Types

---

# Data Types

String
Integer
Float
Boolean
None

---

# Numerical Operators

---

# Numerical Operators

```python
print(1 + 2) # Addition / Concatenation
print(5 - 3) # Subtraction
print(3 * 7) # Multiplication
print(49 / 7) # Division
print(4 ** 2) # Exponent
print(10 % 3) # Modulus (Remainder)
```

---

# Comments

---

# Comments
```python
# The total including VAT
total = sub_total + vat

has_paid = False # If the user has paid or not
```

---

# Casting

---

# Casting

```python
x = int(8.3)  # x will be 8
y = float(9)  # y will be 9.0
z = str(10.0) # z will be '10.0'
```

---

# Index

---

# Index

| C | H | A | R | L | I | E |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |


```python
name = "CHARLIE"
print(name[0]) # Prints 'C'
print(name[1]) # Prints 'H'
```

---

# Input

---

# Input

```python
name = input("What's your name? ")
print("Hello " + name)

age = int(input("How old are you? "))
age_in_10_years = age + 10
print("In 10 years you will be " + str(age_in_10_years))
```

---

# Conditionals

---

# If

---

# If

```python
if True:
    print("This is always shown")

if False:
    print("This is never shown")    
```

---

# If

```python
if <expression>:
    # Will only be run if the expression is True
    <code>
```

---

# Comparators

| Comparator |  Description | Example |
|--- | --- | --- |
| == | Equals | "Alice" == "Alice"
| != | Does not equal | "Bob" != "Charlie"
| < | Less than | 4 < 10
| > | Greater than | 12 > 8
| <= | Less than or equal to | 7 <= 7
| >= | Greater than or equal to | 8 >= 5

---

# Comparators

[.code-highlight: 1-6]
[.code-highlight: 8-10]
```python
name = "Alice"
if name == "Alice":
    print("Hello Alice")

if name != "Charlie":
    print("You are not Charlie")

age = 24
if age >= 21:
    print("You are 21 or over")
```

---

# Else

---

# Else

```python
if 1 == 1:
    print("Yes")
else:
    print("No")    
```

---

# Else

```python
if <expression>:
    # Will only be run if the expression is True
    <code>
else:
    # Will only be run if the expression is False
    <code>
```

---

# Else

[.code-highlight: 1-5]
[.code-highlight: 7-11]
```python
name = "Alice"
if name == "Alice":
    print("Hello Alice")
else:
    print("You are not Alice")

age = 24
if age >= 21:
    print("You are 21 or over")
else:
    print("You are 20 or younger")
```

---

# [fit]Coding Time
## Section A

---

# Elif

---

# Elif

```python
name = "Bob"
if name == "Alice":
    print("Hello Alice")
elif name == "Bob":
    print("Hello Bob")
else:
    print("You must be Charlie")
```

---

# Elif

```python
age = int(input("How old are you? "))
if age <= 13:
    print("You are 13 or younger")
elif age < 18:
    print("You are between 14 and 17")
elif age == 18:
    print("You are 18")
else:
    print("You are 19 or over")
```

---

# And, Or, Not

---

# And, Or, Not

```python
if age > 12 and age < 20:
    print("You are a teenager")

if age < 13 or age > 19:
    print("You are not a teenager")

if not (age > 12 and age < 20):
    print("You are not a teenager")
```

---

# [fit]Coding Time
## Section B

---

# For Loops

---

# For Loops

```python
for x in range(1, 100):
    print(x)
```

---

# For Loops

```python
for <variable> in <range>:
    # Runs multiple times depending on the range
    <code>
```

---

# Ranges

---

# Ranges

[.code-highlight: 1-2]
[.code-highlight: 4-5]
[.code-highlight: 7-8]
```python
range(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1, 5)
#[1, 2, 3, 4]

range(2000, 2020, 4)
#[2000, 2004, 2008, 2012, 2016]
```

---

# [fit]Coding Time
## Section C

---

# While Loops

---

# While Loops

```python
guess = None
while guess != 4:
    # Continues to ask for a number until you enter 4
    guess = int(input("What's your number? "))
```

---

# While Loops

```python
while <condition>:
    # Runs over and over while condition is True
    <code>
```

---

# Infinite Loops

---

# Infinite Loops

```python
while True:
    # This loops forever
    print("Hello")
```

---

# Break Statements

---

# Break Statements

```python
while True:
    print("Hello")
    break
```

---

# Modules

---

# Modules

```python
import random
from math import floor
```

---

# Modules

```python
import <module>
from <module> import <function>

<rest of code>
```

---

# Random Module

---

# Random Module

```python
import random

# Random float from 0.0 to 1.0
print random.random()

# Gets a random number between 1 and 10
number = random.randint(1, 10)
```

---

# Math Module

---

# Math Module

```python
from math import floor, ceil

number = floor(3.2) # 3
print(floor(9.99)) # 9

number = ceil(3.2) # 4
print(ceil(9.99)) # 10
```

---

# [fit]Coding Time
## Section D

---

# Exercises

Finish off any exercises you did not complete in the session

---

### Further Help

## [fit]DL-UKIHFCode@kpmg.co.uk
