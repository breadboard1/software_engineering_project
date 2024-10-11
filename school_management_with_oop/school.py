class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f"No classroom with name {className}")


    def __repr__(self):
        print("---------------All Classrooms-------------")
        for key, value in self.classrooms.items():
            print(key)
        print("---------------Students---------------")
        eight = self.classrooms['eight']
        for student in eight.students:
            print(student.name)
        # print(len(eight.students))
        print("--------------Subjects------------")
        for subject in eight.subjects:
            print(subject.name,"--->", subject.teacher)
        print("------------Student Exam Marks-----------")
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value)
            print("-----------end of one------------")
        return ""


class ClassRoom:
    def __init__(self, name):
        self.name = name
        # composition
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f"{self.name}-{len(self.students) + 1}"
        student.id = serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

    def __str__(self):
        return f"{self.name}-{len(self.students)}"

    def get_top_student(self):
        pass


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.maxMarks = 100
        self.pass_marks = 30

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
