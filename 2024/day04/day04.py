import re

with open('input.txt', 'r') as file:
    data = file.readlines()
    lines = [list(line.strip()) for line in data]

#---------------
# ans1
#---------------

transposed_matrix = list(map(list, zip(*lines)))

def extract_diagonals(matrix):
    diagonals_lr = []  # Left-to-right diagonals
    diagonals_rl = []  # Right-to-left diagonals
    rows, cols = len(matrix), len(matrix[0])
    
    for d in range(rows + cols - 1):
        diag_lr = []
        diag_rl = []
        for i in range(max(0, d - cols + 1), min(d + 1, rows)):
            diag_lr.append(matrix[i][d - i])  # Left-to-right diagonal
            diag_rl.append(matrix[i][cols - 1 - (d - i)])  # Right-to-left diagonal
        diagonals_lr.append(diag_lr)
        diagonals_rl.append(diag_rl)
    
    return diagonals_lr, diagonals_rl

diagonals_lr, diagonals_rl = extract_diagonals(lines)

ans1 = 0

def count_matches(lines, patterns):
    count = 0
    for line in lines:
        line_str = ''.join(line)  # Convert line to string
        for pattern in patterns:
            count += len(re.findall(pattern, line_str))
    return count

patterns = [r"XMAS", r"SAMX"]

ans1 += count_matches(data, patterns)
ans1 += count_matches([''.join(row) for row in transposed_matrix], patterns)
ans1 += count_matches(diagonals_lr, patterns)
ans1 += count_matches(diagonals_rl, patterns)
print(ans1)

#---------------
# ans2
#---------------

check = []
ans2 = 0

for i in range(len(data)-2):
    for j in range(len(data[i]) - 2):
        check.extend([data[i][j], data[i][j+2], data[i+1][j+1], data[i+2][j], data[i+2][j+2]])
        if "".join(check) in ["MMASS", "MSAMS", "SMASM", "SSAMM"]:
            ans2 += 1
        check = []

print(ans2)


