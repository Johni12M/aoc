with open("input.txt", "r") as f:
    file_content = f.read().strip()

counter = 0
total_sum = 0

lst = [char for char in file_content if char.isdigit()]
n = len(lst)

i = 0
while i < n:
    next_index = (i + 1) % n

    if lst[i] == lst[next_index]:
        total_sum += int(lst[i])
        counter += 2
        i += 2
    else:
        counter += 1
        i += 1

print(f"Total Sum: {total_sum}")


