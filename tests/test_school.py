from pytest import raises
from unittest.mock import Mock
from your_module_name import Classroom, Teacher, Student, TooManyStudents

# Test adding a student to a classroom
def test_add_student():
    teacher = Teacher("Professor McGonagall")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "Transfiguration"
    classroom = Classroom(teacher, students, course_title)

    new_student = Student("Harry Potter")
    classroom.add_student(new_student)

    assert len(classroom.students) == 11
    assert new_student in classroom.students

# Test adding too many students to a classroom
def test_add_too_many_students():
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "Potions"
    classroom = Classroom(teacher, students, course_title)

    with raises(TooManyStudents):
        classroom.add_student(Student("Ron Weasley"))

# Test removing a student from a classroom
def test_remove_student():
    teacher = Teacher("Professor Flitwick")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "Charms"
    classroom = Classroom(teacher, students, course_title)

    student_to_remove = students[3].name
    classroom.remove_student(student_to_remove)

    assert len(classroom.students) == 9
    assert student_to_remove not in [student.name for student in classroom.students]

# Test changing the teacher of a classroom
def test_change_teacher():
    initial_teacher = Teacher("Professor Binns")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "History of Magic"
    classroom = Classroom(initial_teacher, students, course_title)

    new_teacher = Teacher("Professor Dumbledore")
    classroom.change_teacher(new_teacher)

    assert classroom.teacher == new_teacher

# Test that the Person class initializes correctly
def test_person_init():
    name = "Severus Snape"
    person = Person(name)
    assert person.name == name
