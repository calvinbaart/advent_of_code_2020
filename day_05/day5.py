def process(line):
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("L", "0")
    line = line.replace("R", "1")

    row = int(line[:7], base=2)
    column = int(line[7:], base=2)

    return [row, column, (row * 8) + column]

def part1(input, initial_value = 0, method = max):
    highest_id = initial_value

    for line in input:
        _, _, seat = process(line)

        highest_id = method(highest_id, seat)
    
    return highest_id

def part2(input):
    ids = []

    for line in input:
        _, _, seat = process(line)

        ids.append(seat)

    ids.sort()

    for x in range(1, len(ids) - 1):
        if ids[x] + 1 != ids[x + 1]:
            return ids[x] + 1
    
    return -1

input = [x.rstrip("\n") for x in open("input.txt", "r").readlines()]

print(part1(input))
print(part2(input))