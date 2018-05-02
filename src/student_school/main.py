from src.student_school.student import Student
from src.student_school.hs_student import HighSchoolStudent

students = []

james = Student("james")
students.append(james)

carol = Student("carol")
students.append(carol)

ethan = HighSchoolStudent("Ethan")
students.append(ethan)

for student in students:
    print(student.get_name_capitalize())