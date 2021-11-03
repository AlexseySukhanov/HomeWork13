import human
"""
Class descirbes student
"""
class Student(human.Human):
    def __init__(self, name, surname, birthdate, idnumber, regeadres, unversity,):
        super().__init__(name, surname, birthdate, idnumber, regeadres)
        self.university = unversity


    def __str__(self):
        return f'{super().__str__()}' \
               f'University: {self.university}\n'

