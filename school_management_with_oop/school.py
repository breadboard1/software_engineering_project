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

    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f"No classroom with name {classroom_name}")


class ClassRoom:
    def __init__(self, name):
        self.name = name
        # composition
        self.students = []

    def add_student(self, student):
        serial_id = f"{self.name}-{len(self.students) + 1}"
        student.id = serial_id
        self.students.append(student)
        self.classroom = self.name

    def __str__(self):
        return f"{self.name}-{len(self.students)}"

    def get_top_student(self):
        pass
