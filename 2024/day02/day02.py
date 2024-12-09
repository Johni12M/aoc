data = [i.strip() for i in open("input.txt")]

ans1 = 0
ans2 = 0

def check(a):
    y = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    if (min(y) > 0 and max(y) < 4) or (min(y) > -4 and max(y) < 0):
        return 1
    return 0


for j in input:
    x = [int(i) for i in j.split()]
    ans1 += check(x)
    m = 0
    for i in range(len(x)):
        z = x[:i] + x[i+1:]
        if check(z) == 1:
            ans2 +=1
            break
print(ans1)
print(ans2)
