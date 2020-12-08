input = open("part_1.txt", "r").readlines()
valid = 0

for data in input:
    before, password = data.split(":")

    before = before.strip()
    password = password.strip()

    index, character = before.split(" ")
    index1, index2 = index.split("-")

    index1 = int(index1) - 1
    index2 = int(index2) - 1

    if password[index1] != character and password[index2] != character:
        continue

    if password[index2] == character and password[index1] == character:
        continue

    valid += 1

print(valid)