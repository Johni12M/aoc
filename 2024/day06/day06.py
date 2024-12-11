data = [i.strip() for i in open("input.txt")]

grid = {}
visited = set()

for r in range(len(data)):
    for c in range(len(data[0])):
        grid[(r, c)] = data[r][c]
        if data[r][c] not in "#.":
            start = (r, c)

visited.add(start)


if grid[start] == "^": dr, dc = -1, 0
if grid[start] == ">": dr, dc = 0, 1
if grid[start] == "v": dr, dc = 1, 0
if grid[start] == "<": dr, dc = 0, -1

p = (start[0], start[1])
print(start)
print(dr, dc)

while True:
    new = (p[0]+dr,p[1]+dc)
    if new not in grid:
        break
    else:
        if grid[new] == "#":
            dr, dc = dc, -dr
        else:
            p = (new)
            visited.add(p)


print(len(visited))

