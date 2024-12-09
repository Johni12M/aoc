with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# 1000x1000 grid initialized with brightness 0
grid = [0] * (1000 * 1000)

for line in lines:
    line_split = line.split(" ")
    
    if line.startswith("turn on"):
        start = list(map(int, line_split[2].split(",")))
        end = list(map(int, line_split[4].split(",")))
        
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                grid[x + y * 1000] += 1  # Increase brightness by 1
    
    elif line.startswith("turn off"):
        start = list(map(int, line_split[2].split(",")))
        end = list(map(int, line_split[4].split(",")))
        
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                grid[x + y * 1000] = max(0, grid[x + y * 1000] - 1)  # Decrease brightness, but not below 0
    
    elif line.startswith("toggle"):
        start = list(map(int, line_split[1].split(",")))
        end = list(map(int, line_split[3].split(",")))
        
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                grid[x + y * 1000] += 2  # Increase brightness by 2

# Sum up all brightness values
print(sum(grid))

