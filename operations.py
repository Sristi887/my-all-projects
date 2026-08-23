def display_all_students(studentslist):
    for roll_no in studentslist:
        print(roll_no, studentslist[roll_no].name, studentslist[roll_no].marks)


def display(studentslist, roll_no):
    try:
        print(f"Student name: {studentslist[roll_no].name}, Student marks: {studentslist[roll_no].marks}")  
    except KeyError:
        print("Student not found.")



def update_marks(studentslist, roll_no, new_marks):
    try:
        studentslist[roll_no].marks = new_marks
    except KeyError:
        print("Student not found.")


def delete_student(studentslist, roll_no):
    try:
        del studentslist[roll_no]
        print(f"Student with roll number {roll_no} has been deleted.")
    except KeyError:
        print("Student not found.")
