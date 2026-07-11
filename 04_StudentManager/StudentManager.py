# Manages students and their grades
class Student:

    # Initializes a new Student object
    def __init__(self, student_id, name, grade):
        self.name = name
        self.student_id = str(student_id)
        self.grade = float(grade)

    # Returns a formatted string representation of the student
    def __str__(self):
        return f"[{self.student_id:7s}] {self.name:20s}    {self.grade:.1f}"


class Control:

    # Dictionary that stores all students
    # Key: student ID, Value: Student object
    students = {}

    # Creates a Control object and starts the program execution
    def __init__(self):
        self.run()

    # Adds a new student to the students dictionary
    def add_student(self):
        data = input(
            "Enter student data ID,NAME,GRADE (press enter to finish): "
        ).split(",")

        print(data)

        try:
            # Check that exactly three values were entered
            if len(data) != 3:
                print("Invalid number of values.")
                return

            student_id = data[0].strip()
            name = data[1].strip()
            grade = data[2].strip()

            # Validate student ID:
            # It must contain exactly 7 digits
            if not student_id.isdigit() or len(student_id) != 7:
                print("Student ID must contain exactly 7 digits.")
                return

            # Validate grade:
            # It must be a number between 0 and 10
            try:
                grade_value = float(grade)

            except:
                print("Grade must be a number.")
                return

            if grade_value < 0 or grade_value > 10:
                print("Grade must be between 0 and 10.")
                return

            # Check if student ID already exists
            if student_id in Control.students.keys():

                while True:
                    answer = input(
                        "Student ID already exists. "
                        "Do you want to overwrite the student? (Yes/No): "
                    )

                    if answer == "Yes":
                        Control.students[student_id] = Student(student_id, name, grade)
                        print("Student updated.")
                        break

                    elif answer == "No":
                        print("Operation cancelled.")
                        break

                    else:
                        print("Please answer Yes or No.")

            else:
                # Create and store a new student object
                Control.students[student_id] = Student(student_id, name, grade)

                print("Student added. Total students:", len(Control.students))

        except:
            print("Invalid data.")

    # Deletes a student from the dictionary
    def delete_student(self):

        student_id = input("Enter student ID to delete (press enter to finish): ")

        print(student_id)

        try:
            if student_id in Control.students.keys():

                del Control.students[student_id]
                print("Student deleted.")

            else:
                print("Student not found.")

        except:
            print("Invalid data.")

    # Display students sorted by student ID
    def show_students(self):

        for student in sorted(
            Control.students.values(), key=lambda student: student.student_id
        ):
            print(student)

    # Main program loop
    # Displays the available commands and waits for user input
    def run(self):

        while True:

            print(
                "\nAdd student (+), Delete student (x), "
                "Show students (?), Enter to exit"
            )

            choice = input("...")

            if not choice:
                break

            elif choice == "+":
                self.add_student()

            elif choice == "x":
                self.delete_student()

            elif choice == "?":
                self.show_students()


# Start program
if __name__ == "__main__":
    Control()
