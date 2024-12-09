data = [i.strip() for i in open("input.txt")]

rules = []
updates = []

for line in data:
    if "|" in line:
        rules.append(line)
    elif line:
        updates.append(line.split(','))

def is_correct_order(update, rules):
    for rule in rules:
        before, after = rule.split('|')
        if before in update and after in update:
            index1 = update.index(before)
            index2 = update.index(after)
            if index1 > index2:
                return False
    return True

def fix_order(update, rules):
    while True:
        changed = False
        for rule in rules:
            before, after = rule.split('|')
            if before in update and after in update:
                index1 = update.index(before)
                index2 = update.index(after)
                if index1 > index2:
                    update[index1], update[index2] = update[index2], update[index1]
                    changed = True
        if not changed:
            break
    return update

sum_of_middles = 0
for update in updates:
    if not is_correct_order(update, rules):
        fixed_update = fix_order(update, rules)
        mid_index = len(fixed_update) // 2
        sum_of_middles += int(fixed_update[mid_index])

print("Summe der mittleren Seiten:", sum_of_middles)


