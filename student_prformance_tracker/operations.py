# def display_all_students(studentslist):
#     for roll_no in studentslist:
#         print(roll_no, studentslist[roll_no].name, studentslist[roll_no].marks)


# def display(studentslist, roll_no):
#     try:
#         print(f"Student name: {studentslist[roll_no].name}, Student marks: {studentslist[roll_no].marks}")  
#     except KeyError:
#         print("Student not found.")



# def update_marks(studentslist, roll_no, new_marks):
#     try:
#         studentslist[roll_no].marks = new_marks
#     except KeyError:
#         print("Student not found.")


# def delete_student(studentslist, roll_no):
#     try:
#         del studentslist[roll_no]
#         print(f"Student with roll number {roll_no} has been deleted.")
#     except KeyError:
#         print("Student not found.")

import sqlite3

import sqlite3


def add_student_with_marks(Roll_no, name, subjects_marks):
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    try:
        # Add student
        cursor.execute(
            "INSERT INTO student (Roll_no, name) VALUES (?, ?)",
            (Roll_no, name)
        )

        # Add all subjects and marks
        for subject, marks in subjects_marks:
            cursor.execute(
                "INSERT INTO marks (Roll_no, subject, marks) VALUES (?, ?, ?)",
                (Roll_no, subject, marks)
            )

        # Save everything together
        connection.commit()
        print("Student and marks added successfully.")

    except sqlite3.Error as e:
        connection.rollback()
        print("Error:", e)

    connection.close()

def display(Roll_no):
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name FROM student WHERE Roll_no = ?",
        (Roll_no,)
    )

    student = cursor.fetchone()

    cursor.execute(
        "SELECT subject, marks FROM marks WHERE Roll_no = ?",
        (Roll_no,)
    )

    marks_result = cursor.fetchall()

    if student:
        print("Student name:", student[0])

        for subject, marks in marks_result:
            print(subject, marks)
    else:
        print("Student not found.")

    connection.close()


def update_marks(Roll_no, subject, new_marks):
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE marks SET marks = ? WHERE Roll_no = ? AND subject = ?",
        (new_marks, Roll_no, subject)
    )

    if cursor.rowcount == 1:
        print("Marks updated successfully.")
    else:
        print("Student/subject not found.")

    connection.commit()
    connection.close()


def delete_student(Roll_no):
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    try:
        # Delete all marks of the student
        cursor.execute(
            "DELETE FROM marks WHERE Roll_no = ?",
            (Roll_no,)
        )

        # Delete the student
        cursor.execute(
            "DELETE FROM student WHERE Roll_no = ?",
            (Roll_no,)
        )

        if cursor.rowcount == 1:
            connection.commit()
            print("Student and all marks deleted successfully.")
        else:
            connection.rollback()
            print("Student not found.")

    except sqlite3.Error as e:
        connection.rollback()
        print("Error:", e)

    connection.close()

def display_all_students():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT student.Roll_no, student.name, marks.subject, marks.marks
        FROM student
        LEFT JOIN marks
        ON student.Roll_no = marks.Roll_no
    """)

    students = cursor.fetchall()

    for Roll_no, name, subject, marks in students:
        if subject is None:
            print(Roll_no, name, "No marks recorded")
        else:
            print(Roll_no, name, subject, marks)

    connection.close()