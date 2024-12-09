with open("input.txt", "r") as file:
    input_data = file.readlines()

processed_lines = [line.split("   ") for line in input_data]

processed_lines = [line for line in processed_lines if len(line) == 2]

left_side = [int(element[0]) for element in processed_lines]
right_side = [int(element[1]) for element in processed_lines]


score = 0
for i in range(len(processed_lines)):
    score += left_side[i] * right_side.count(left_side[i])

print("Left side (sorted):", left_side)
print("Right side (sorted):", right_side)
print("Total differences:", score)
