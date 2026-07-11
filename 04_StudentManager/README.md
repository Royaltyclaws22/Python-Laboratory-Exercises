# 🎓 Student Manager

Α simple Python command-line application for managing student records, allowing users to add, view, and delete students while validating IDs and grades.


## 🔎 Preview



## ⚙️ Features

- Add new students with:
  - Student ID
  - Name
  - Grade
- Validate student ID format (exactly 7 digits)
- Validate grades (range: 0-10)
- Prevent duplicate student IDs
- Update an existing student after confirmation
- Display all students sorted by student ID
- Delete students by student ID
- Simple command-line interface


## 💻 Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/Royaltyclaws22/Python-Laboratory-Exercises.git
```
2. Navigate to the project folder:
```bash
cd Python-Laboratory-Exercises/04_StudentManager
```
3. Run the program:
```bash
python StudentManager.py
```


## 💡 Usage

Run the program and select an operation from the menu:

```text
Add student (+), Delete student (x), Show students (?), Enter to exit
```

### (+) Adding a student

Press `+` and enter the student's information in the following format:

```text
StudentID,Name,Grade
```

**Example:**

```text
1234567,John Smith,8.5
```

The program checks:
- If the Student ID contains exactly 7 digits
- If the grade is a number between 0 and 10
- If the Student ID already exists

If the Student ID already exists, the user is asked whether they want to update the existing student.


### (x) Deleting a student

Press `x` and enter the Student ID of the student you want to remove.

**Example:**

```text
Enter student ID to delete (press enter to finish): 1234567
```

If the student exists, they are removed from the list.


### (?) Viewing students

Press `?` to display all registered students. Students are displayed sorted by Student ID.

**Example:**

```text
[1234567] John Smith                    8.5
[2345678] Mary Brown                    9.0
```


### Exiting the program

Press `Enter` without typing a command to close the application.
