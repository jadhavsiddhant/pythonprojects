
students = {}

def add_student():
    rollno = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[rollno] = {'Name': name, 'Marks': marks}
    print(f"Student {name} added successfully!")

def display_students():
    if not students:
        print("No students to display.")
    else:
        for rollno, details in students.items():
            print(f"Roll No: {rollno}, Name: {details['Name']}, Marks: {details['Marks']}")

def search_student():
    rollno = input("Enter Roll Number to search: ")
    if rollno in students:
        print(f"Found: Roll No: {rollno}, Name: {students[rollno]['Name']}, Marks: {students[rollno]['Marks']}")
    else:
        print("Student not found.")

def remove_student():
    rollno = input("Enter Roll Number to remove: ")
    if rollno in students:
        del students[rollno]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def total_students():
    print(f"Total number of students: {len(students)}")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Display Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        remove_student()
    elif choice == '5':
        total_students()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
