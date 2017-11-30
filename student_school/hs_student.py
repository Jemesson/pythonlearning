from student_school.student import Student


class HighSchoolStudent(Student):
    school_name = "Decisao"

    def get_school_name(self):
        return self.school_name

    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"
