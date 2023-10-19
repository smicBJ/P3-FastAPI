
# Typing is the action of explicitly stating what type we will use for a definition
def greeting(name: str):
    # While typing, the methods for the object of a string show up as a result of us declaring this type would be a str
    new_greeting = f"Hello {name.lower()}"
    return new_greeting


# Examples of a list
def add(my_list: list[int]):
    response = 0
    for item in my_list:
        response += item
    return response


# Example of a parameter that might be null or another type
def give_phone(phone_number: str | None):
    if phone_number is not None:
        print(phone_number)
    else:
        print("No Number given")


give_phone(phone_number="407-954-1234")


# We can also create a custom class_info to act as a type for a paramater:
class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


richard = Person(name="Richard", age=17)
print(richard)


# Just like with the standard types, we get access to the attributes and methods while defining our class_info
def register_user(person: Person):
    print(person.name)


# The following line of code will fail as a result of it not having the name attr, not because it isn't the right type:
# => register_user(person={"name": "richard"})

# This is why it is important to note, this is not actually a way to validate code in your actual function definitions
register_user(person=richard)

