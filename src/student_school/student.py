class Student:
    def __init__(self, name, id=123):
        self.name = name
        self.id = id

    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()
