input = [x.rstrip("\n") for x in open("input.txt", "r").readlines()]

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

total_num_open = 0
total_num_tree = 0

for slope in slopes:
    x = 0
    num_open = 0
    num_tree = 0

    for y in range(slope[1], len(input), slope[1]):
        x += slope[0]

        if input[y][x % len(input[y])] == ".":
            num_open += 1
        elif input[y][x % len(input[y])] == "#":
            num_tree += 1
    
    if total_num_open == 0:
        total_num_open = num_open
        total_num_tree = num_tree
    else:
        total_num_open *= num_open
        total_num_tree *= num_tree

print("%s %s" % (total_num_open, total_num_tree))