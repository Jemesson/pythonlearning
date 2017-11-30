from student_school.student import Student
from student_school.hs_student import HighSchoolStudent

student = Student("Jemesson")
print(student.get_name_capitalize() + " " + student.get_school_name())

student = HighSchoolStudent("Jemesson")
print(student.get_name_capitalize() + " " + student.get_school_name())