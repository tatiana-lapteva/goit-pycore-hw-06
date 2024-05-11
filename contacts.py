

from collections import UserDict

class Field:
    def __init__(self, value: str) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    

class Name(Field):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        

class Phone(Field):

    def __init__(self, phone: str) -> None:
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError("invalid phone number")
    
    def __str__(self) -> str:
        return str(self.value)


class Record:
    
    def __init__(self, name: str) -> None:
        self.name = Name(name)   
        self.phones: list[Phone] = []
        self.record = {self.name: self.phones}
        
    def add_phone(self, phone: str) -> None:
        if phone not in self.phones:
            self.phone = Phone(phone)
            self.phones.append(self.phone)
        else:
            raise ValueError("phone {phone} already exists in contact")


    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]
        
                

    def edit_phone(self, phone: str, new_phone: str) -> None:
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones[index] = Phone(new_phone).value
            


    def find_phone(self, phone: str) -> str:
        for p in self.phones:
            if p.value == phone:
                return phone

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, \
            phones: {';'.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
        
    def add_record(self, record: Record) -> None:
        if record.name.value in self.data:
            self.data.update({record.name.value: record})
        else:
            self.data[record.name.value] = record

    def find(self, name: str) -> list[Phone]:
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError(f"Contact {name} not in Contats")
        
    
    def find_phone(phone: str) -> str:
        name.find_phone(phone)


    def edit_phone(phone: str, new_phone: str) -> None:
        name.edit_phone(phone, new_phone)


    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact {name} not in the contacts")



# create new address book
book = AddressBook()

# create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# add record John to address book
book.add_record(john_record)


#create and add new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")

# add record Jane to address book
book.add_record(jane_record)


# show all records in the book
for name, record in book.data.items():
    print(record)


# search John's phones
john = book.find("John")

# edit John's phone
john.edit_phone("1234567890", "1112223333")

print(john)

#find requested phone in record John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  


# delete record Jane
book.delete("Jane")


