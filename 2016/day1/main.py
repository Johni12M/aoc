with open('input.txt') as f:
    instructions = f.read().strip()

start = (0, 0)
end = [(0, 0)]
degree = 0
distance = None

for i in instructions.split(","):
    i = i.strip()
    direction = i[0]
    steps = int(i[1:])

    if direction == "L":
        degree = (degree + 90) % 360
    elif direction == "R":
        degree = (degree - 90) % 360

    for _ in range(steps):
        last_position = end[-1]
        if degree == 0:
            new_position = (last_position[0], last_position[1] + 1)
        elif degree == 90:
            new_position = (last_position[0] + 1, last_position[1])
        elif degree == 180:
            new_position = (last_position[0], last_position[1] - 1)
        elif degree == 270:
            new_position = (last_position[0] - 1, last_position[1])

        end.append(new_position)

        if end.count(new_position) == 2 and distance is None:
            distance = abs(start[0] - new_position[0]) + abs(start[1] - new_position[1])

if distance is not None:
    print(f"Erste doppelte Position: {distance}")
else:
    print("Keine doppelte Position gefunden.")

