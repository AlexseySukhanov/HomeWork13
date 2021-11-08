from student import Student
from ie import IE
"""
Class describes group of students
"""


class Group:

    def __init__(self, groupname, students):
        try:
            if len(students) > 10:
                raise IE(len(students), "Amount of students can't be more than 10 ")
        except IE as error:
            return error

        self.groupname = groupname
        self.group = students

    def find(self, surn):
        for i in self.group:
            if i.surname == surn:
                return f'Name: {i.name} ID Number: {i.idnumber}'

    def rem(self, idnum):
        for i in range(len(self.group)):
            if self.group[i].idnumber == idnum:
                return self.group.pop(i)


    def __str__(self):
        s =" ".join([i.surname for i in self.group])
        # for i in self.group:
        #     s += str(i.surname)+" "
        return s
