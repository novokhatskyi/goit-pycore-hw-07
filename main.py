from parse_input import parse_input
from add_contacts import add_contacts, change_contacts, get_phone, get_all_contacts, add_birthday, get_all_birthdays, show_birthday
from AddressBook import AddressBook


def main():
    book = AddressBook()
    # book ={}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        args = args[0] if args else []

        if command in ["close", "exit", "пока"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts(args, book))
        elif command == "change":
            print(change_contacts(args, book))
        elif command == "phone":
            print(get_phone(args,book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "get-birthdays":
            print(get_all_birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
