from flask import Flask, request, render_template


app = Flask(__name__)
students = [
    {
        "id": 1,
        "name": "Ali",
        "course": "AI",
        "email": "ali@gmail.com"
    },
    {
        "id": 2,
        "name": "Ahmed",
        "course": "Python",
        "email": "ahmed@gmail.com"
    },
    {
        "id": 3,
        "name": "Sara",
        "course": "Flask",
        "email": "sara@gmail.com"
    },
    {
        "id": 4,
        "name": "Ayesha",
        "course": "GenAI",
        "email": "ayesha@gmail.com"
    }
]

@app.route("/")
def home():
    return "Welcome to Student Enrollment System"

@app.route("/student/<int:student_id>")
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}

@app.route("/students")
def get_students():
    course = request.args.get("course")

    if course:
        filtered_students = []

        for student in students:
            if student["course"].lower() == course.lower():
                filtered_students.append(student)

        return filtered_students

    return students

@app.route("/add-student-form", methods=["POST"])
def add_student_form():

    student_id = request.form.get("id")
    name = request.form.get("name")
    course = request.form.get("course")
    email = request.form.get("email")

    # Validation
    if not student_id or not name or not course or not email:
        return {"message": "All fields are required"}

    new_student = {
        "id": int(student_id),
        "name": name,
        "course": course,
        "email": email
    }

    students.append(new_student)

    return {
        "message": "Student added successfully",
        "student": new_student
    }

@app.route("/add-student-json", methods=["POST"])
def add_student_json():

    data = request.get_json()

    if not data:
        return {"message": "No JSON data received"}

    student_id = data.get("id")
    name = data.get("name")
    course = data.get("course")
    email = data.get("email")

    if not student_id or not name or not course or not email:
        return {"message": "All fields are required"}

    new_student = {
        "id": student_id,
        "name": name,
        "course": course,
        "email": email
    }

    students.append(new_student)

    return {
        "message": "Student added successfully",
        "student": new_student
    }

@app.route("/students-page")
def students_page():
    return render_template("students.html", students=students)

@app.route("/student-page/<int:student_id>")
def student_page(student_id):

    student = None

    for s in students:
        if s["id"] == student_id:
            student = s
            break

    return render_template("student.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)