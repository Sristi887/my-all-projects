class student:
    def __init__(self, name, marks):
        
        self.name = name
        self.marks = marks

studentslist = {}

option = input("Do you want to load existing student data from file? (yes/no): ").strip().lower()
if option == "yes":
    with open("student.txt", "r") as f:
        for line in f:
            roll_no, name, marks = line.strip().split(",")
            roll_no = int(roll_no)
            marks = float(marks)
            obj = student(name, marks)
            studentslist[roll_no] = obj

else:
    n = int(input("How many students? "))


    for _ in range(n):
        roll_no = int(input("Enter the student's unique roll number: "))
        name = input("Enter the student's name: ")
        marks = float(input("Enter the student's marks: "))
        obj = student(name, marks)

        studentslist[roll_no] = obj



import operations

def menu():

    choice = 0
    while choice != 5:

        print("Enter 1 to display all student details")
        print("Enter 2 to display a particular student's marks")
        print("Enter 3 to update student marks")
        print("Enter 4 to delete a student")
        print("Enter 5 to exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            operations.display_all_students(studentslist)

        elif choice == 2:
            roll_no = int(input("Enter the roll number of the student: "))
            operations.display(studentslist, roll_no)

        elif choice == 3:
            roll_no = int(input("Enter the roll number of the student: "))
            new_marks = float(input("Enter new marks: "))
            operations.update_marks(studentslist, roll_no, new_marks)

        elif choice == 4:
            roll_no = int(input("Enter the roll number of the student to delete: "))
            operations.delete_student(studentslist, roll_no)

        elif choice == 5:
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please try again.")



menu()

with open("student.txt", "w") as f:
    for roll_no in studentslist:
        f.write(f"{roll_no},{studentslist[roll_no].name},{studentslist[roll_no].marks}\n")

