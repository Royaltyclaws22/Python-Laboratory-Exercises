# Define note names
NOTE_NAMES = [
    "Do",
    "Do#",
    "Re",
    "Re#",
    "Mi",
    "Fa",
    "Fa#",
    "Sol",
    "Sol#",
    "La",
    "La#",
    "Si",
]

# Create frequency dictionary
notes = {}

# Set reference frequency
A4 = 440
SEMITONE_RATIO = 2 ** (1 / 12)

# Generate lower notes
freq = A4
i = 0

while freq >= 20:
    rounded_freq = int(freq + 0.5)

    note_name = NOTE_NAMES[(9 - i) % 12]
    octave = 4 + ((9 - i) // 12)

    notes[rounded_freq] = note_name + str(octave)

    i += 1
    freq = A4 / (SEMITONE_RATIO**i)


# Generate higher notes
i = 1

while True:
    freq = A4 * (SEMITONE_RATIO**i)

    if freq > 22000:
        break

    rounded_freq = int(freq + 0.5)

    note_name = NOTE_NAMES[(9 + i) % 12]
    octave = 4 + ((9 + i) // 12)

    notes[rounded_freq] = note_name + str(octave)

    i += 1


# Find the closest note frequency
def closest_note_freq(freq):

    closest = None
    smallest_difference = float("inf")

    # Compare all note frequencies
    for note_freq in notes:
        difference = abs(note_freq - freq)

        # Select closest or lower frequency
        if difference < smallest_difference or (
            difference == smallest_difference and note_freq < closest
        ):
            smallest_difference = difference
            closest = note_freq

    return closest


# Run the program
def main():

    while True:
        try:
            frequency = int(input("Enter frequency (0 to exit): "))

            # Stop program
            if frequency == 0:
                break

            # Check input range
            if frequency < 20 or frequency > 22000:
                print("Frequency must be between 20Hz and 22000Hz.")
                continue

            nearest_frequency = closest_note_freq(frequency)

            print(
                f"Closest Note: {notes[nearest_frequency]} " f"({nearest_frequency}Hz)"
            )

        except ValueError:
            print("Enter a valid integer.")


# Start program
if __name__ == "__main__":
    main()
