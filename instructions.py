from action import (add_persone, append_phone, change_phone, delete_phone,
                    hello_message, searcher, show_all, show_part, show_phone)
from birthday_action import select_birthday_date, when_birthday

instructions = '''
Add a new contact: "add" /contact name/ /contact phone/
Change phone for a contact: "change" /contact name/ /new contact phone/
Add new phone for contact: "append" /contact name/ /new contact phone/
Delete the phone for contact: "pop" /contact name/
See the contact's phone number: "phone" /contact name/
Set a birthday for a contact: "birthday" /contact name/
Get information about the contact's birthday: "party" /contact name/
View all contacts: "show all"
View N elements of the notebook: "part" /N/
Search by records: "search" /search phrase/

See this message again: "help"
'''


def get_help():
    print(instructions)


USER_INPUT = {
    'hello': hello_message,
    'add': add_persone,
    'change': change_phone,
    'phone': show_phone,
    'pop': delete_phone,
    'append': append_phone,
    "show all": show_all,
    "part": show_part,
    'birthday': select_birthday_date,
    'help': get_help,
    'party': when_birthday,
    'search': searcher
}
