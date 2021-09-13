class Person:
    name = "Глеб"
    age = 51

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course = 1

    def set(self, name, age, course):
            self.name = name
            self.age = age
            self.course = course

sasha = Student ("Вася", 28)
# sasha.set ("Саша", 28)
sasha.set("Саша", 23, 5)
print ("Имя: ", sasha.name, ", возраст - ", sasha.age, ", курс - ", sasha.course)

vadim = Person ("Вадим", 25)
# vadim.set ("Вадим", 25)
print (vadim.name + " " + str(vadim.age))

gleb = Person ("Глеб", 19)
# gleb.set ("Глеб", 19)
print (gleb.name + " " + str(gleb.age))
