with open("input.txt", "r", encoding="utf-8") as file:
    input_data = file.readlines()

processed_lines = [line.split("\n") for line in input_data]

print(processed_lines)
