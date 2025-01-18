from faker import Faker
from re import sub

fk = Faker("id-ID")


class Contact:
    def __init__(self, name: str, number: str):
        self._name = name
        self._number = number

    def show(self):
        output = ""
        output += sub(r"(?<!^)(?=[A-Z])", " ", f"{self.__class__.__name__}\n")
        for key, value in self.__dict__.items():
            if not key.__contains__("__"):
                output += f"{key[1:].capitalize()}: {value}\n"
        return output

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if f"_{key}" in self.__dict__:
                self.__dict__[f"_{key}"] = value


class PersonalContact(Contact):
    def __init__(self, name: str, number: str, email: str, address: str):
        super().__init__(name, number)
        self.__email = email
        self.__address = address

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str) -> None:
        self.__address = address


class BusinessContact(Contact):
    def __init__(self, name: str, number: str, company: str, job: str):
        super().__init__(name, number)
        self.__company = company
        self.__job = job

    def get_company(self) -> str:
        return self.__company

    def set_company(self, company: str) -> None:
        self.__company = company

    def get_job(self) -> str:
        return self.__job

    def set_job(self, job: str) -> None:
        self.__job = job


class ContactManager:
    def __init__(self):
        self.__contact = []

    def index(self):
        return self.__contact

    def create(self, contact: Contact):
        self.__contact.append(contact)

    def search(self, query: str):
        output = []
        for c in self.__contact:
            if query in c._name:
                output.append(c)
        return output

    def update(self, name: str, **kwargs):
        for c in self.__contact:
            if c._name == name:
                c.update(**kwargs)
                break

    def destroy(self, name: str):
        for i, c in enumerate(self.__contact):
            if c._name == name:
                del self.__contact[i]
                break
