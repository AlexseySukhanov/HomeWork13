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
            return IE

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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.group):
            self.index +=1
            return self.group[self.index-1]
        else:
            raise StopIteration



    def __str__(self):
        s =" ".join([i.surname for i in self.group])

        return s
