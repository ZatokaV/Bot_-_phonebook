from classes import ADDRESS_BOOK, Name, Phone, Record
from decorators import input_error


def hello_message():
    print("How can I help you?")


@input_error
def add_persone(user_message):

    name = Name(user_message)
    phone = Phone(user_message)
    record = Record(name, phone)

    if len(user_message.split(' ')) != 3:
        print('Enter correct name and phone')
        return False
    if name.value in ADDRESS_BOOK:
        print(f'{name.value.capitalize()} is already in the phone book')
        return False
    if Phone.vallide_phone(phone.value):
        ADDRESS_BOOK.add_record(record)
        print(f'A contact {name.value.capitalize()} has been added '
              f'to the phone book. Phone(s) {phone.value}')


@input_error
def change_phone(user_message):

    name = Name(user_message)
    phone = Phone(user_message)
    record = Record(name, phone)

    if len(user_message.split(' ')) != 3:
        print('when changing phone, use the "change /name/ /phone/" template')
        return False
    if name.value in ADDRESS_BOOK and Phone.vallide_phone(phone.value):
        record.replace_phone(name, phone)
        print(f'{name.value.capitalize()} phone has been '
              f'changed to {phone.value}')
    if name.value not in ADDRESS_BOOK:
        print(f'{name.value.capitalize()} is not in the phone book. '
              f'You cannot change its number')


@input_error
def append_phone(user_message):

    name = Name(user_message)
    phone = Phone(user_message)
    record = Record(name, phone)

    if len(user_message.split(' ')) != 3:
        print('Enter correct name and phone')
        return False
    if name.value not in ADDRESS_BOOK:
        print(
            f'{name.value.capitalize()} is not in the phone book. '
            f'You cannot added number for it')
        return False
    if Phone.vallide_phone(phone.value):
        record.add_phone(name, phone)
        print(f'For {name.value.capitalize()} added phone {phone.value}')


@input_error
def show_phone(user_message):

    name = Name(user_message)

    if len(user_message.split(' ')) != 2:
        print('when searching for a number, use the template "phone" "name"')
        return False
    if name.value in ADDRESS_BOOK:
        for users in ADDRESS_BOOK.values():
            if name.value == users.name.value:
                print(
                    f'Name: {users.name.value.capitalize()}, '
                    f'Phone: {users.phones.value}')
    else:
        print(f'Name {name.value.capitalize()} is not in the phone book')


@input_error
def delete_phone(user_message):

    name = Name(user_message)

    if len(user_message.split(' ')) != 2:
        print('when delete phone for contact, use the "pop name"')
        return False
    if name.value in ADDRESS_BOOK:
        for users in ADDRESS_BOOK.values():
            users.remove_phone(users, name)


def show_all():

    print('Your contact list:')

    for users in ADDRESS_BOOK.values():
        print(users)


@input_error
def show_part(user_message):

    count = user_message.split(' ')[1]
    page = ADDRESS_BOOK.iterator()

    while True:
        try:
            show_next = input(f'\nShow {count} contacts? (y/n)\n')
            if show_next == 'y':
                for _ in range(int(count)):
                    print(next(page))
            if show_next == 'n':
                break
        except StopIteration:
            print('Book is over')
            break


def searcher(user_message):

    part_for_search = user_message.split(' ')[1]

    for users in ADDRESS_BOOK.values():
        for el in users.phones.value:
            if part_for_search in el:
                print(users)
        if part_for_search in users.name.value:
            print(users)
