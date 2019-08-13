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



[
    {
        "fname": "bob",
        "lname": "smith",
        "age": 54,
        kids: [t
            {
                "fname": "Jane",
                "lname": "smith",
                "age": 12,
                "kids": None
            },
            {
                "fname": "Chris",
                "lname": "smith",
                "age": 21,
                "kids": [

                ]
            },
        ]
    }

]
