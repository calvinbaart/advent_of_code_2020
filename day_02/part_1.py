input = open("part_1.txt", "r").readlines()
valid = 0

for data in input:
    before, password = data.split(":")

    before = before.strip()
    password = password.strip()

    length, character = before.split(" ")
    min_length, max_length = length.split("-")

    min_length = int(min_length)
    max_length = int(max_length)

    num_occurences = len([x for x in password if x == character])

    if num_occurences < min_length or num_occurences > max_length:
        continue

    valid += 1

print(valid)