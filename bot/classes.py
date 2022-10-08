import pickle
from collections import UserDict
from datetime import datetime
from string import ascii_letters


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):

    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
        self._value = self.vallide_phone(value)

    @staticmethod
    def vallide_phone(phone):
        if len(phone[0]) < 10 or len(phone[0]) > 17:
            print('Phone must be 10-17 characters without letters')
            return False
        for i in phone[0]:
            if i in ascii_letters:
                print('Phone must be 10-17 characters without letters')
                return False

        return phone


class Birthday(Field):

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
        self._value = self.vallide_day(value)

    @staticmethod
    def vallide_day(person_birthday):

        today = datetime.now()

        if person_birthday > datetime.date(today):
            return False
        return person_birthday


class Record:

    def __init__(self, name: Name, phones: Phone, birthday: Birthday = None):
        self.name = name
        self.phones = phones
        self.birthday = birthday

    def add_phone(self, name, phone):
        for users in ADDRESS_BOOK.values():
            if name.value == users.name.value:
                users.phones.value.append(phone.value[0])

    def replace_phone(self, name: Name, phone: Phone):
        for users in ADDRESS_BOOK.values():
            if name.value == users.name.value:
                users.phones.value = phone.value

    def remove_phone(self, users, name):
        if name.value == users.name.value:
            users.phones.value.pop()
            print(f'Phone number for contact {name.value.capitalize()} '
                  f'is deleted')

    def add_birthday(self, birth: datetime):
        if self.birthday is None:
            birth = Birthday(birth)
            self.birthday = birth
        else:
            while True:
                qwestion = input('Change birthday for contact?\n(y/n)')
                if qwestion == 'y':
                    birth = Birthday(birth)
                    self.birthday = birth
                    break
                if qwestion == 'n':
                    break

    def days_to_birthday(self, original_date, now):
        self.original_date = self.birthday
        self.now = datetime.now()
        delta1 = datetime(now.year, original_date.month, original_date.day)
        delta2 = datetime(now.year+1, original_date.month, original_date.day)
        self.days = ((delta1 if delta1 > now else delta2) - now).days
        return self.days

    def __repr__(self):
        if not self.birthday:
            return str(f'{self.name.value.capitalize()}, {self.phones.value}')
        else:
            return str(f'{self.name.value.capitalize()}, {self.phones.value}, '
                       f'Birthday: {self.birthday.value}')


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self):
        for record in self.data.values():
            yield record

    def write_contacts_to_file(self):
        with open('data_notebook.txt', 'wb') as file:
            pickle.dump(self.data, file)

    def read_contacts_from_file(self):
        try:
            with open('data_notebook.txt', 'rb') as file:
                contacts_archive = pickle.load(file)
                return contacts_archive
        except FileNotFoundError:
            pass


ADDRESS_BOOK = AddressBook()
