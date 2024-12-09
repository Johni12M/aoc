nice_strings = 0

with open('input.txt') as f:
    strings = f.read().splitlines()

for string in strings:
    # Condition 1: Check for non-overlapping pairs
    has_pair = False
    pairs = {}
    for i in range(len(string) - 1):
        pair = string[i:i+2]
        if pair in pairs and pairs[pair] < i - 1:
            has_pair = True
            break  # No need to continue once we find a valid pair
        pairs[pair] = i

    # Condition 2: Check for repeating letter with a gap
    has_repeating_letter = False
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            has_repeating_letter = True
            break  # No need to continue once we find the repeating letter

    # Only count the string if both conditions are met
    if has_pair and has_repeating_letter:
        nice_strings += 1

print(nice_strings)

