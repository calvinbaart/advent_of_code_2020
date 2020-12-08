input = [int(x) for x in open("part_1.txt", "r").readlines()]

for x in range(0, len(input)):
    for y in range(0, len(input)):
        for z in range(0, len(input)):
            if x == y or x == z or y == z:
                continue

            if input[x] + input[y] + input[z] != 2020:
                continue

            print(input[x] * input[y] * input[z])
            exit()