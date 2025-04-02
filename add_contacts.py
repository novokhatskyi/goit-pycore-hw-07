from colorama import Fore
from errors import input_error
from AddressBook import Field, Birthday, Phone, Record, AddressBook, Name

@input_error
def add_contacts(args, book: AddressBook):
    # print(f"DEBUG: Отримані аргументи: {args}")
    if len(args) !=2:
        return "Не правильно введено ім\'я та номер телефону"
    name, phone = args
    record = book.find_name(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        record.add_phone(Phone(phone))
        return f"Contact {Fore.BLUE}{name}{Fore.RESET} added!"
    else:
        return f"Контакт з таким імям {Fore.BLUE}{name}{Fore.RESET} вже існує, тому додано додатковий номер"

@input_error
def change_contacts(args,book: AddressBook):
    # if len(args) !=2:
    #     return "Не правильно введено і\'я та номер телефону"
    name, old_phone, new_phone = args
    record = book.find_name(name)
    if record is None:
        return f"Контакт {Fore.GREEN}{name}{Fore.RESET} не знайдено в списку контактів"
    else:
        record.edit_phone(Phone(old_phone), Phone(new_phone))
        return f"Контакт {Fore.RED}{name}{Fore.RESET} оновлено"

@input_error
def get_phone(args, book: AddressBook):
    # if len(args) !=1:
    #     return "Помилка введення запиту. Потрібно ввести тільки ім\'я"
    name = args[0]
    record = book.find_name(name)
    record_phones = []
    if record is None:
        return f"Контакт {name} не знайдено в списку контактів"
    else:
        for phone in record_phones:
            record_phones.append(phone.value)
            phones = ",".join(record_phones)
        return f"Номер телефону контакту {Fore.YELLOW}{name}{Fore.RESET} - {phones}"
    
# @input_error    
def get_all_contacts(book: AddressBook):
    
    # record = book.find_name(name)
    result =[]
    for record in book.values():
        contact_info = {
            "name": record.name.value,
            "phone": [phone.value for phone in record.phones]
        }
        if record.birthday:
            contact_info["birthday"] = record.birthday.value
        result.append(contact_info)
    return result
    
@input_error    
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find_name(name)
    if record is not None:
        record.add_birthday(Birthday(birthday))
        return f"День народження додано до контаку {record.name.value}"
    else:
        return f"УПС. Контакту з іменем {name} не знайдено."

@input_error      
def show_birthday (args, book):
    name = args[0]
    record = book.find_name(name)
    if record is None:
        return f"УПС, конаткт з іменем {name} не знайдено"
    else:
        return f"""Та буде тобі відомо, що {Fore.YELLOW}{name}{Fore.RESET}
        народилася {record.get_birthday().value}"""
    
@input_error      
def get_all_birthdays(args, book:AddressBook):
    birthdays = book.get_upcoming_birthdays()
    results =[]
    if not birthdays:
        return "В найближчий час днів народження не буде"
    else:
        for birthday in birthdays:
            results.append(f"{birthday['name']} — {birthday['congratulation_date']}")
        return results








if __name__== "__main__" :
    pass
    