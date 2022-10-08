from datetime import datetime

from classes import ADDRESS_BOOK, Birthday, Name
from decorators import input_error


@input_error
def select_birthday_date(user_message):

    name = Name(user_message.split(' ')[1])

    if len(user_message.split(' ')) != 2:
        print('Error. Enter "birthday" "name"')
        return False
    if name.value in ADDRESS_BOOK:
        birthday = input('Enter YYYY/MM/DD''\n').split('/')
        person_birthday = datetime(year=int(birthday[0]), month=int(
            birthday[1]), day=int(birthday[2]))
        person_birthday = datetime.date(person_birthday)
        for users in ADDRESS_BOOK.values():
            if (users.name.value == name.value
                    and Birthday.vallide_day(person_birthday)):
                users.add_birthday(person_birthday)
                print(f'For contact {users.name.value.capitalize()} '
                      f'added birthray {users.birthday.value}')
        if not Birthday.vallide_day(person_birthday):
            print('Incorrect date, try again')
    else:
        print(f'{name.value} birthray not in adress book')


@input_error
def when_birthday(user_message):

    name = Name(user_message.split(' ')[1])

    if len(user_message.split(' ')) != 2:
        print('when searching for a number, use the template "party" "name"')
        return False
    if name.value in ADDRESS_BOOK:
        for users in ADDRESS_BOOK.values():
            if name.value == users.name.value and users.birthday is not None:
                days = users.days_to_birthday(
                    users.birthday.value, datetime.now())
                print(
                    f'Name: {users.name.value.capitalize()}, '
                    f'Birthday: {users.birthday.value}, after {days} days')
            if name.value == users.name.value and users.birthday is None:
                print('This contact does not have a date of birth')
    else:
        print(f'Name {name.value.capitalize()} is not in the phone book')
