# 📝 MyNotes

A simple command-line note manager written in Python which allows users to create, save, and view notes organized by month and year.


## 🔎 Preview
<img width="1280" height="720" alt="THIS" src="https://github.com/user-attachments/assets/2d193662-d6ec-47a7-a7b0-13084dee7e79" />


## ⚙️ Features

- Create new notes with a selected date or use today's date automatically.
- Automatically saves notes into monthly `.txt` files.
- Organizes notes by month and year.
- Displays saved notes for a selected month.
- Simple interactive command-line menu.


## 💻 Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/Royaltyclaws22/Python-Laboratory-Exercises.git
```
2. Navigate to the project folder:
```bash
cd Python-Laboratory-Exercises/02_MyNotes
```
3. Run the program:
```bash
python MyNotes.py
```

## 💡 Usage

After starting the program, choose an option from the menu:

```text
=== myNotes ===
Options:
1. View notes
2. New note
3. Exit
```

### 1) View notes

Select:

```text
1. View notes
```
by typing the number '1'.

Enter the month in the format:

```text
MM-YYYY
```

**Example:**

```text
07-2026
```

The program will display all notes saved for that month.


### 2) Create a new note

Select:

```text
2. New note
```
by typing the number '2'.

Enter a date using the format:

```text
DD-MM-YYYY
```

**Example:**

```text
08-07-2026
```

Press **Enter** without entering a date to use today's date.
Type your notes line by line. Press **Enter** on an empty line to save the note.


### 3) Exit the program

Select:

```text
3. Exit
```
by typing the number '3' when you are done. Your notes are saved automatically into monthly `.txt` files that can be found in the same folder as the `MyNotes.py` file.
