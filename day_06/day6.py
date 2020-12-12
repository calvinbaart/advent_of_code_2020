def part1(input):
    input = [set("".join(x)) for x in input]
    return sum([len(x) for x in input])

def parse_group(group):
    current = set(group[0])

    for index in range(1, len(group)):
        current = current.intersection(set(group[index]))
    
    return current

def part2(input):
    input = ["".join(parse_group(x)) for x in input]
    return sum([len(x) for x in input])

input = [x.replace("\n", " ").split(" ") for x in open("sample_input.txt", "r").read().split("\n\n")]

print(part1(input))
print(part2(input))