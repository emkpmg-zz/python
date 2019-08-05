names = []

name = None

while name != "":
    name = input("Whats your name? ")

    if name:
        age = input("How old? ")
        names.append({
            "name": name,
            "age": int(age)
        })

for person in names:
    print(person['name'] + " is " + str(person['age']))
