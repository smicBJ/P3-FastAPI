

def greeting(name: str):
    new_greeting = f"Hello {name.capitalize()}"
    return new_greeting


def add(my_list: list[int]):
    response = 0
    for item in my_list:
        response += item
    return response


def give_phone(phone_number: str | None):
    if phone_number is not None:
        print(phone_number)
    else:
        print("No Number given")


give_phone("405")
