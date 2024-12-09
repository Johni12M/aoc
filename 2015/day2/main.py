with open("input.txt") as r:
    input = r.read().splitlines()

paper = 0
ribbon = 0

for line in input:
    line = line.split("x")
    l, w, h = int(line[0]), int(line[1]), int(line[2])
    sides = (2*l*w)+(2*w*h)+(2*h*l)
    sides_sorted = sorted([l, w, h])
    extra = sides_sorted[0] * sides_sorted[1]
    sides += extra
    paper += sides
    ribbon += (l*w*h) + (2*sides_sorted[0]) + (2*sides_sorted[1])

print(paper)
print(ribbon)

