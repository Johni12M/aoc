with open ("input.txt", "r") as file:
    input = file.read()

floor = 0
counter = 0

for letter in input:
    if letter == "(":
        floor += 1
        counter += 1
    elif letter == ")":
        floor -= 1
        counter += 1
        if floor == -1:
            print(counter)
            break
    else:
        print("Error")
print(floor)                
