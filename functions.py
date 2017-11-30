import os

students = []


def read_students(f):
    yield from f


def read_file():
    try:
        file = open("student.txt", "r")
        for student in read_students(file):
            add_student(student)
        file.close()
    except IOError:
        print("could not read the file")


def write_file(student):
    try:
        file = open("student.txt", "a")
        file.write(student + "\n")
        file.close()
    except IOError:
        print("could not write in file")


def get_students_name():
    names = []
    for student in students:
        names.append(student["name"].title())
    return names


def print_students():
    print(get_students_name())


def add_student(name, student_id=123):
    student = {
        "id": student_id,
        "name": name
    }

    students.append(student)


if not os.path.exists("student.txt"):
    open('student.txt', 'xt')

read_file()
print_students()

while True:
    try:
        ask = input("Do you want to add a student? (Y/N) ")
        ask = ask.strip().upper()

        if ask == "N":
            break
        elif ask == "Y":
            id = input("Enter student id: ")
            student_name = input("Enter student name: ")

            add_student(student_name, int(id))
            write_file(student_name)
        else:
            print("Sorry add again.")

    except KeyboardInterrupt as e:
        print("Say me please.")

print_students()
