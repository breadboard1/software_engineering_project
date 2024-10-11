from school import School, ClassRoom, Subject
from persons import Student, Teacher

def main():
    school = School('Kuri kinder garden', 'charia')

    eight = ClassRoom('eight')
    school.add_classroom(eight)

    nine = ClassRoom('nine')
    school.add_classroom(nine)

    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('abul ali kabul', eight)
    school.student_admission(abul)

    babul = Student('babul ali babul', eight)
    school.student_admission(babul)

    kubbul = Student('kubul ali kubbul', eight)
    school.student_admission(kubbul)

    # subjects
    topon_sir = Teacher('Shahjahan topon')
    physics = Subject('physics', topon_sir)
    eight.add_subject(physics)

    haradhon_sir = Teacher('Naga haradhon')
    chemistry = Subject('chemistry', haradhon_sir)
    eight.add_subject(chemistry)

    azmol_sir = Teacher('Gazi azmol')
    biology = Subject('biology', azmol_sir)
    eight.add_subject(biology)

    eight.take_semester_final()

    print(school)







if __name__ == "__main__":
    main()