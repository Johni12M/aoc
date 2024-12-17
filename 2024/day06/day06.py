data = [i.strip() for i in open("test.txt")]

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

p = ((start[0], start[1]), (dr, dc))
print(start)
print(dr, dc)

def path(pos, deltar, deltac):
    loops = 0
    while True:
        print("the beginning")
        new = (pos[0][0]+deltar,pos[0][1]+deltac)
        print(new)
        if new not in grid:
            break
        else:
            if (new, (deltar, deltac)) in visited:
                loops += 1
                continue
            if grid[new] == "#":
                deltar, deltac = deltac, -deltar
                continue
            else:
                pos = ((new),(deltar, deltac))
                visited.add(pos)
                print("the end")
    print("loops:", loops)
    return loops
path(p, dr, dc)
print(len(visited))
print(visited)

while True:
    for i in range(len(visited)-1):
        position = visited[i]
        grid[visited[i+1][0]] = "#"
        path(position, position[1][0], position[1][1])
        print(i)


