from student_school.student import Student


class HighSchoolStudent(Student):
    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"
