input = [int(x) for x in open("part_1.txt", "r").readlines()]

for x in range(0, len(input)):
    for y in range(0, len(input)):
        if x == y:
            continue

        if input[x] + input[y] != 2020:
            continue

        print(input[x] * input[y])
        exit()