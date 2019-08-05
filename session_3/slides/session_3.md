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

# For Loops

```python
for x in range(1, 100):
    print(x)
```

---

# While Loops

```python
guess = None
while guess != 4:
    # Continues to ask for a number until you enter 4
    guess = int(input("What's your number? "))
```

---

# Collections

---

# Collections — List

```python
names = ["Alice", "Bob", "Charlie"]
print(names[0]) # Alice
print(names[1]) # Bob
print(names[2]) # Charlie
```

---

# List — Add

```python
names = ["Alice", "Bob", "Charlie"]

# Append a new value to the end of the list
names.append("Dave")

print(names) # ["Alice", "Bob", "Charlie", "Dave"]

```

---

# List — Change

```python
names = ["Alice", "Bob", "Charlie"]

# Change the value stored in index 2
names[2] = "Chris"

print(names) # ["Alice", "Bob", "Chris"]

```

---

# List — Delete

```python
names = ["Alice", "Bob", "Charlie"]

# Delete the item at index 1
del(names[1])

print(names) # ["Alice", "Charlie"]

```

---

# List — In

```python
names = ["Alice", "Bob", "Charlie"]

# Check to see if "Eve" is in the list
if "Eve" in names:
    print("Eve is here")
else:
    print("Eve isn't here")
```

---

# List — Length

```python
names = ["Alice", "Bob", "Charlie"]

# Get the number of items in the list
print(len(names)) # 3
```

---

# List — Sort

```python
names = ["Charlie", "Alice", "Bob"]

# Sort the items in the list alphabetically
names.sort()

print(names) # ["Alice", "Bob", "Charlie"]
```

---

# List — For

```python
names = ["Alice", "Bob", "Charlie"]

for person in names:
    print(person)
```

---

# [fit]Coding Time
## Section A

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

# Dictionary — Add

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
    "colour": "Red",
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


# Exercises

Finish off any exercises you did not complete in the session

---

### Further Help

## [fit]DL-UKIHFCode@kpmg.co.uk
