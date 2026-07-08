import datetime
import os

# print("\nCurrent folder:", os.getcwd())

# Weekday names mapping
w_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday", 
}


# Create and save a new note
def add_note():

    # Set note date
    mydate = input("Note date (DD-MM-YYYY), <enter> for today: ")

    if mydate == "":
        mydate = datetime.datetime.now().strftime("%d-%m-%Y")

    try:
        day, month, year = map(int, mydate.split("-"))

        note_date = datetime.date(year, month, day)
        weekday = note_date.weekday()

    except ValueError:
        print("Invalid date format")
        return

    weekday_name = w_days[weekday]

    # Create filename based on month and year
    script_folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_folder, f'{month:02d}-{year}.txt')

    # Save note header and content
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"#{mydate} {weekday_name}\n")

        while True:
            nt = input("Note: ")

            # Empty input ends note entry
            if nt == "":
                break

            f.write(nt + "\n")

    print("Note saved successfully.")


# Display notes for a selected month
def overview():

    month = input("Month (MM-YYYY): ")
    filename = month + ".txt"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())

    except FileNotFoundError:
        print("No notes found for this month.")


# Main application menu
def menu():

    while True:
        print("\n=== myNotes ===")
        print("Options:")
        print("1. View notes")
        print("2. New note")
        print("3. Exit")

        reply = input(">>> ")

        if reply == "3":
            break

        elif reply == "1":
            overview()

        elif reply == "2":
            add_note()

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
