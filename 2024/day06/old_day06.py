import re

with open("input.txt", "r") as file:
    data = file.readlines()

char_data = [list(line.strip()) for line in data]

print("Eingelesene Daten:")
print(char_data)

pattern = r"[><\^v]"
guard = []
for row_idx, row in enumerate(char_data):
    for col_idx, char in enumerate(row):
        if char in "^v<>":
            guard.append([row_idx, col_idx, char])

print("Gefundene Koordinaten und Richtungen:")
print(guard)

def count_X_in_data():
    return sum(row.count("X") for row in char_data)

directions = ["^", ">", "v", "<"]

visited_positions = set()  # Set, um besuchte Positionen zu speichern

if guard:
    while True:
        row, col, direction = guard[0]

        if row < 0 or col < 0 or row >= len(char_data) or col >= len(char_data[0]):
            print("Index außerhalb des Rasters! Anzahl der 'X':", count_X_in_data())
            break

        visited_positions.add((row, col, direction))  # Position speichern

        if char_data[row][col] == "#":
            current_direction_index = directions.index(direction)
            next_direction = directions[(current_direction_index + 1) % 4]  # Dreht sich zur nächsten Richtung
            guard[0][2] = next_direction  # Neue Richtung setzen

        if direction == "^":
            if row <= 0 or char_data[row - 1][col] == "#":  # Überprüfen auf Rand oder '#'
                continue  # Wächter dreht sich, falls er auf ein '#' stößt
            guard[0][0] -= 1  # Wächter geht nach oben
            char_data[guard[0][0]][guard[0][1]] = "X"

        elif direction == ">":
            if col >= len(char_data[0]) - 1 or char_data[row][col + 1] == "#":  # Überprüfen auf Rand oder '#'
                continue  # Wächter dreht sich, falls er auf ein '#' stößt
            guard[0][1] += 1  # Wächter geht nach rechts
            char_data[guard[0][0]][guard[0][1]] = "X"

        elif direction == "v":
            if row >= len(char_data) - 1 or char_data[row + 1][col] == "#":  # Überprüfen auf Rand oder '#'
                continue  # Wächter dreht sich, falls er auf ein '#' stößt
            guard[0][0] += 1  # Wächter geht nach unten
            char_data[guard[0][0]][guard[0][1]] = "X"

        elif direction == "<":
            if col <= 0 or char_data[row][col - 1] == "#":  # Überprüfen auf Rand oder '#'
                continue  # Wächter dreht sich, falls er auf ein '#' stößt
            guard[0][1] -= 1  # Wächter geht nach links
            char_data[guard[0][0]][guard[0][1]] = "X"

print("Anzahl der X in den Daten:", count_X_in_data())
