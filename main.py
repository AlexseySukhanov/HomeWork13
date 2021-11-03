from human import Human
from student import Student
from group import Group
import datetime

#считываем информацию о людях из файла
human=[]
f=open('humans.txt')
readhum=f.readlines()
f.close()
for i in range(len(readhum)):
    readhum[i] = readhum[i].replace("\n","")
    readhum[i] = readhum[i].split("@")
    dat=readhum[i][2].split(" ") # формируем дату
    human.append(Human(readhum[i][0], readhum[i][1], datetime.date(int(dat[0]),int(dat[1]),int(dat[2])), int(readhum[i][3]), readhum[i][4]))

for i in range(len(human)):
    print(human[i])

# создаем инстанс класса студент
students=[]
for i in range(len(human)):
    students.append(Student(human[i].name,human[i].surname,human[i].birthdate,human[i].idnumber,human[i].regadres,"NTUU"))

for i in range(len(students)):
    print(students[i])

#создаем инстанс класса группа

gr=Group("VV-51",students)
print(Group.find(gr,"Ivanov"))

print(Group.rem(gr,2755325145))

print(gr)

