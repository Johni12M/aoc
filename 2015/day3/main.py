with open("input.txt") as r:
    input_data = r.read()

# Initialize positions
house_santa = [0, 0]
house_robot = [0, 0]
houses_visited = {tuple(house_santa)}  # Initialize with starting position, use a set for unique values
move_number = 0

# Function to update the position based on the current direction
def move(position, direction):
    if direction == "^":
        position[1] += 1
    elif direction == "v":
        position[1] -= 1
    elif direction == ">":
        position[0] += 1
    elif direction == "<":
        position[0] -= 1
    return position

# Iterate through the directions in the input
for letter in input_data:
    if move_number % 2 == 0:  # Santa's turn
        house_santa = move(house_santa, letter)
        houses_visited.add(tuple(house_santa))  # Add to set for unique visits
    else:  # Robot's turn
        house_robot = move(house_robot, letter)
        houses_visited.add(tuple(house_robot))  # Add to set for unique visits

    move_number += 1  # Increment move number

# Print the number of unique houses visited by both Santa and the robot
print(len(houses_visited))

