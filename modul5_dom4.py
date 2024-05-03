def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Key error occurred. Please enter valid input."
        except ValueError:
            return "Value error occurred. Please enter valid input."
        except IndexError:
            return "Index error occurred. Please enter valid input."
    return inner

def parse_input(command):
    parts = command.split()
    keyword = parts[0].lower()
    args = parts[1:]

    return keyword, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(args, contacts):
    if len(args) == 0:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "Invalid command."
    
def main():
    contacts = {}

    while True:
        command = input("Enter command: ")
        keyword, args = parse_input(command)
        if keyword == "hello":
            print("How can I help you?")
        elif keyword == "add":
            print(add_contact(args, contacts))
        elif keyword == "change":
            print(change_contact(args, contacts))
        elif keyword == "phone":
            print(show_phone(args, contacts))
        elif keyword == "all":
            print(show_all(args, contacts))
        elif keyword == "exit" or keyword == "close":
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
