from classes import ADDRESS_BOOK
from instructions import USER_INPUT, instructions


def main():

    print(instructions)

    notes_in_file = ADDRESS_BOOK.read_contacts_from_file()
    if notes_in_file:
        for key, value in notes_in_file.items():
            ADDRESS_BOOK.data[key] = value

    while True:
        user_message = input('...\n').lower()

        if user_message.endswith(' '):
            user_message = user_message.rstrip()
        if not user_message or user_message.startswith(' '):
            continue

        if user_message in ("good bye", "close", "exit"):
            print("Good bye!")
            ADDRESS_BOOK.write_contacts_to_file()
            break

        if user_message in USER_INPUT:
            USER_INPUT[user_message]()
        elif user_message.split()[0] in USER_INPUT:
            USER_INPUT[user_message.split()[0]](user_message)


if __name__ == '__main__':
    main()
