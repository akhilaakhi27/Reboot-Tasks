def dict():
    person = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "city": input("Enter city: ")
    }
    
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
dict()