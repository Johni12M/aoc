with open("input.txt") as f:
    text = f.read().splitlines()

wires = {}

for line in text:
    line = line.split(" ")
    if line[0].isdigit():
        if line[1] == "->":
            wires[line[2]] = line[0]
print(wires)
