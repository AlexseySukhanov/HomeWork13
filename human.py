"""
Class describes human
"""

class Human:

    def __init__(self, name, surname, birthdate, idnumber, regeadres):
        if not isinstance(name, str):
            raise TypeError(f'{type(name).__name__} Name is not valid')
        if not isinstance(surname, str):
            raise TypeError(f'{type(surname).__name__} Surname is not valid')
        self.name = name.title()
        self.surname=surname.title()
        self.birthdate=birthdate
        self.regadres=regeadres
        self.idnumber=int(idnumber)


    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Surname: {self.surname}\n' \
               f'Date of birth: {self.birthdate}\n' \
               f'ID number: {self.idnumber}\n' \
               f'Registration adress: {self.regadres}\n'

