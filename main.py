# from operations import add_student, add_marks, display, display_all_students, update_marks, delete_student

# class student:
#     def __init__(self, name, marks):
        
#         self.name = name
#         self.marks = marks

# studentslist = {}

# option = input("Do you want to load existing student data from file? (yes/no): ").strip().lower()
# if option == "yes":
#     with open("student.txt", "r") as f:
#         for line in f:
#             roll_no, name, marks = line.strip().split(",")
#             roll_no = int(roll_no)
#             marks = float(marks)
#             obj = student(name, marks)
#             studentslist[roll_no] = obj

# else:
#     n = int(input("How many students? "))


#     for _ in range(n):
#         roll_no = int(input("Enter the student's unique roll number: "))
#         name = input("Enter the student's name: ")
#         marks = float(input("Enter the student's marks: "))
#         obj = student(name, marks)

#         studentslist[roll_no] = obj


import operations


def menu():

    while True:

        print("\n--- Student Performance Tracker ---")
        print("1. Add student")
        print("2. Display all students")
        print("3. Display a student")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            Roll_no = int(input("Enter roll number: "))
            name = input("Enter student name: ")

            n = int(input("Enter number of subjects: "))

            subjects_marks = []

            for i in range(n):

                subject = input(f"Enter subject {i + 1}: ")
                marks = int(input(f"Enter marks for {subject}: "))

                subjects_marks.append((subject, marks))

            operations.add_student_with_marks(
                Roll_no,
                name,
                subjects_marks
            )

        elif choice == 2:
            operations.display_all_students()

        elif choice == 3:
            Roll_no = int(input("Enter roll number: "))

            operations.display(Roll_no)

        elif choice == 4:
            Roll_no = int(input("Enter roll number: "))
            subject = input("Enter subject: ")
            new_marks = int(input("Enter new marks: "))

            operations.update_marks(Roll_no, subject, new_marks)

        elif choice == 5:
            Roll_no = int(input("Enter roll number: "))

            operations.delete_student(Roll_no)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


menu()

    

# with open("student.txt", "w") as f:
#     for roll_no in studentslist:
#         f.write(f"{roll_no},{studentslist[roll_no].name},{studentslist[roll_no].marks}\n")

