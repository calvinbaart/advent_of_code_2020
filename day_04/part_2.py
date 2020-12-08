import string

input = [x.replace("\n", " ") for x in open("input.txt", "r").read().split("\n\n")]

num_valid = 0
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

required_fields = {
    "byr": lambda x: 
        int(x) >= 1920 and int(x) <= 2002,

    "iyr": lambda x: 
        int(x) >= 2010 and int(x) <= 2020,

    "eyr": lambda x: 
        int(x) >= 2020 and int(x) <= 2030,

    "hgt": lambda x: 
        (int(x[:-2]) >= 150 and int(x[:-2]) <= 193) if x[-2:] == "cm" else 
        (int(x[:-2]) >= 59 and int(x[:-2]) <= 76) if x[-2:] == "in" else 
        False,

    "hcl": lambda x: 
        x[0] == "#" and 
        x[1:].lower() == x[1:] and 
        all(c in string.hexdigits for c in x[1:]),

    "ecl": lambda x: 
        x in eye_colors,

    "pid": lambda x: 
        x.isdigit() and len(x) == 9
}

for passport in input:
    invalid = False
    num_fields = 0

    for data in passport.split(" "):
        identifier, value = data.split(":")

        if identifier not in required_fields:
            continue

        num_fields += 1

        if not required_fields[identifier](value):
            invalid = True
            break

    if invalid or num_fields != len(required_fields):
        continue

    num_valid += 1

print(num_valid)