input = [x.rstrip("\n") for x in open("input.txt", "r").readlines()]

x = 0
num_open = 0
num_tree = 0

for y in range(1, len(input)):
    x += 3

    if input[y][x % len(input[y])] == ".":
        num_open += 1
    elif input[y][x % len(input[y])] == "#":
        num_tree += 1

print("%s %s" % (num_open, num_tree))