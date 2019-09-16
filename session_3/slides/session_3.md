# [fit] IHF: Code
## Python — Session 3

---

# Review

---

# If / Else / Elif

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

# List

```python
names = ["Alice", "Bob", "Charlie"]

print(names[1]) # Bob

names.append("Dave") # ["Alice", "Bob", "Charlie", "Dave"]

names[2] = "Chris" # ["Alice", "Bob", "Chris", "Dave"]

del(names[1])# ["Alice", "Chris", "Dave"]

if "Eve" in names:
    print("Eve is here")

for name in names:
    print(name)
```

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

# For Loops

```python
names = ["Alice", "Bob", "Charlie"]

for person in names:
    print(person)

# Alice
# Bob
# Charlie
```

---

# For Loops

```python
for olympic_years in range(1896, 2020, 4):
    print(olympic_years)

# ...
# 2008
# 2012
# 2016
```

---

# [fit]Questions?

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

# While Loops

```python
times_in_loop = 0
while times_in_loop <= 10:
    print("Hello")
    times_in_loop = times_in_loop + 1
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

# [fit]Coding Time
## Section A

---

# Collections

---

# Collections

List

Tuple

Set

Dictionary

---

# Collections — Tuple

```python
colours = ("Red", "Blue", "Green")
print(colours[0]) # Red
print(colours[1]) # Blue
print(colours[2]) # Green
```

---

# Collections — List Vs Tuple

A tuple is the same as list except you can't change it after creation.

---

# Collections — Set

```python
fruit = {"Apple", "Banana", "Cherry"}
for item in fruit:
    print(item)
```

---

# Collections — Dictionary

```python
shirt = {
    "size": "Large",
    "colour": "Red",
    "material": "Cotton"
}
print(shirt["size"]) # Large
print(shirt["colour"]) # Red
print(shirt["material"]) # Cotton
```

---

# Dictionary — Append

```python
shirt = {
    "size": "Large",
    "colour": "Red"
}

# Add a new key/value
shirt["material"] = "Cotton"
```

---

# Dictionary — Change

```python
shirt = {
    "size": "Large",
    "colour": "Red",
    "material": "Cotton"
}

# Change the colour of the shirt
shirt["colour"] = "Green"
```

---

# Dictionary — Delete

```python
shirt = {
    "size": "Large",
    "colour": "Red",
    "material": "Cotton"
}

# Delete the key/value
del(shirt["size"])
```

---

# Dictionary — In

```python
shirt = {
    "size": "Large",
    "colour": "Red"
}

# Check to see if the key "material" exists in the dictionary
if "material" in shirt:
    print("The material is: " + shirt["material"])

```

---

# Dictionary — For

```python
shirt = {
    "size": "Large",
    "colour": "Red",
    "material": "Cotton"
}

for key in shirt:
    print(str(key) + " = " + str(shirt[key]))
```

---

# Collections

| Collection |  Ordered | Changeable | Duplicates | Key |
|--- | --- | --- | --- | --- |
| List | Yes | Yes | Yes | No
| Tuple | Yes | No | Yes | No
| Set | No | Yes | No | No
| Dictionary | No | Yes | No | Yes

---

# [fit]Coding Time
## Section B

---

# Nested Collections

---

# Nested Collections

```python
phone_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

for row in phone_grid:
    for column in row:
        print(column)
```

---

# List of Dictionaries

```python
contacts = [
    {"fname": "Alice", "lname": "Smith"},
    {"fname": "Bob", "lname": "Jones", "phone": "555-1234"},
    {"fname": "Charlie", "lname": "McCloud"}
]

for person in contacts:
    if "phone" in person:
        print(person["fname"])
```

---

# Adding names

```python
contacts = []
fname = None

while fname != "":
    fname = input("What is your first name? ")
    lname = input("What is your last name? ")

    contacts.append({
        "fname": fname,
        "lname": lname
    })
```

---

# [fit]Coding Time
## Section C

---

Q: Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. Continue to ask for names until no name is given. Then print out all of the names and ages collected.

---

Q: Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. Continue to ask for names until no name is given. Then print out all of the names and ages collected.

```python
contacts = []
fname = None

while fname != "":
    fname = input("What is your first name? ")
    lname = input("What is your last name? ")

    contacts.append({
        "fname": fname,
        "lname": lname
    })
```

---

# Exercises

Finish off any exercises you did not complete in the session

---

### Further Help

## [fit]DL-UKIHFCode@kpmg.co.uk
