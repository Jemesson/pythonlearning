from flask import Flask, render_template, request, redirect, jsonify

from student_school.student import Student

app = Flask(__name__)

students = []


@app.route("/save", methods=["POST"])
def save_student():
    student_id = request.form.get("student_id", "")
    student_name = request.form.get("student_name", "")

    student = Student(name=student_name, id=int(student_id))
    students.append(student)
    return redirect("/")


@app.route("/")
def list_students():
    return render_template("index.html", students=sorted(students, key=lambda student: student.name))


if __name__ == "__main__":
    app.run(debug=True)