students = []


def get_students_name():
    names =[]
    for student in students:
        names.append(student["name"].title())
    return names


def print_students():
    print(get_students_name())


def is_student_valid(student_name, student_id):
    if student_name != "" and student_id != "":
        return True
    return False


def add_student(name, student_id):
    student = {
        "name": name,
        "id": student_id
    }
    students.append(student)


while True:
    try:
        ask = input("Do you want to add a student? (Y/N) ")
        ask = ask.strip().upper()

        if ask == "N":
            break
        elif ask == "Y":
            student_name = input("Enter student name: ")
            student_id = input("Enter student id: ")

            if is_student_valid(student_name, student_id):
                add_student(student_name, student_id)
            else:
                print("Sorry add again.")

    except KeyboardInterrupt as e:
        print("Say me please.")

print(print_students())