input = [x.replace("\n", " ") for x in open("input.txt", "r").read().split("\n\n")]

num_valid = 0

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

for passport in input:
    invalid = False

    for field in required_fields:
        if field not in passport:
            invalid = True
            break

    if invalid:
        continue

    num_valid += 1

print(num_valid)