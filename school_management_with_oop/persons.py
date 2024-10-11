import random

class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        self.subject = subject
        super().__init__(name)

    def teach(self):
        pass

    def take_exam(self, subject, students):
        for student in students:
            marks = random.randint(0, 100)


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__id = None
        self.classroom = None
        self.subjects = []
        self.marks = {}
        self.grade = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value