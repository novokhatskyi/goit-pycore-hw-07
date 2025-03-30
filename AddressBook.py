from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
      def __init__(self, value):
            if value.isdigit() and len(value) == 10:
                super().__init__(value)
            else:
                raise ValueError("Не правильний формат введення номеру, будь-ласка введіть номер з 10 цифр")

class Birthday(Field):
    def __init__(self, value):
        try:
            input_date=datetime.strptime(value, "%d-%m-%Y").date()
            super().__init__(input_date)
        except Exception as e:
            print (f"Дата не відповідає заданому формату і виникаж помилка {e}")
        return None    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone (self, phone: Phone):
        # self.phones = list(filter(lambda p: p.value != phone.value, self.phones))
        new_phone = []
        for p in self.phones:
            if p.value != phone.value:
                new_phone.append(p)
                self.phones = new_phone
        return self.phones
    
    def edit_phone (self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                break
        return self.phones
    
    def search_phone (self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return None
    
    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def get_birthday(self):
        return self.birthday
         
    def __str__(self):
        if self.birthday is not None:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)},birthday: {self.birthday.value}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_name(self, name: str):
        return self.data.get(name)
    
    def dell_name(self, name: str):
        return self.data.pop(name)
    
    def get_upcoming_birthdays(self):
        today = datetime.now().date() 
        upcoming_birthdays = []
        for record in self.data.values():
            birthday_in_list=record.get_birthday().value
            birthday_this_year=birthday_in_list.replace(year=today.year)
            if birthday_this_year<today:
                birthday_this_year=birthday_this_year.replace(year=today.year+1)
            elif today<=birthday_this_year<=today+timedelta(days=7):
                weekday_of_birthday = birthday_this_year.weekday()
                upcoming_birthdays.append({"name":record.name.value, "congratulation_date": birthday_this_year})
            if weekday_of_birthday==5:
                birthday_this_year = birthday_this_year+timedelta(days=+2)
                upcoming_birthdays.append({"name":record.name.value, "congratulation_date": birthday_this_year})
            elif weekday_of_birthday==6:
                birthday_this_year = birthday_this_year+timedelta(days=+1)
                upcoming_birthdays.append({"name":record.name.value, "congratulation_date": birthday_this_year})
        if upcoming_birthdays==[]: # у разі якщо до дня народження більше 7 днів або воно вде минуло - додатково виводитеметься рядок.
            print ("В найбличий термін днів народження не буде")
        else:
            return upcoming_birthdays



if __name__ =="__main__":
    name_1 = Record("Oksana")
    name_1.add_phone(Phone("0973370717"))
    book = AddressBook()
    book.add_record(name_1)
    print(book.data["Oksana"])
    name_1.add_phone(Phone("1234567899"))
    print(book.data["Oksana"])
    name_2 = Record ("Oleksandr")
    name_2.add_phone(Phone("9876054321"))
    book.add_record(name_2)
    print(book)

