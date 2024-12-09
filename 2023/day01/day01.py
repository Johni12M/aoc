import io 
import os

ans1 = 0
ans2 = 0 
valnumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
o = io.open('input.txt').read().strip()
for line in o.split('\n'):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(valnumbers):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    score = int(digits[0]+digits[-1])
    ans2 += score
print(ans2)
