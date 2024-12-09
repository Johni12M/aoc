import re

with open("input.txt", "r") as file:
    data = file.read()

mul = r"mul\((\d+),(\d+)\)"
ans1 = 0
ans2 = 0
do = r"do\(\)"
dont = r"don't\(\)"


matches = re.findall(mul, data)

for value in matches:
    num1, num2 = map(int, value)
    ans1 += num1 * num2
    
print(ans1)

ignore = False
ans2_matches = []

for match in re.finditer(rf"{mul}|{dont}|{do}", data):
    found = match.group()
    if found == "do()":
        ignore = False
    elif found == "don't()":
        ignore = True
    elif not ignore:
        ans2_matches.append(found)


for value in ans2_matches:
    num1, num2 = map(int, value[4:-1].split(","))
    ans2 += num1 * num2

print(ans2)
