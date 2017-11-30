students = []


class Student:
    school_name = "Piaget"

    def __init__(self, name, id = 1):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
