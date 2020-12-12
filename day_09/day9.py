def part1(input, preamble):
    for x in range(preamble, len(input)):
        current = input[x]
        found = False

        for y in range(x - preamble, x):
            wanted = current - input[y]

            if wanted == input[y]:
                continue

            if wanted in input[x - preamble:x]:
                found = True
                break
        
        if not found:
            return (x, current)
                

def part2(input, preamble):
    index, value = part1(input, preamble)
    subset = input[:index]
    
    # there has to be a better algorithm to do this, I found the 0-1 knapsack problem algorithm but that doesn't seem to assume a
    # contiguous set of numbers

    sequence = None

    for x in range(0, len(subset)):
        sequence = [subset[x]]

        for y in range(x + 1, len(subset)):
            if sum(sequence) >= value:
                break
                
            sequence.append(subset[y])
        
        if sum(sequence) == value:
            break
    
    lowest = min(sequence)
    highest = max(sequence)

    return lowest + highest

input = [int(x) for x in open("input.txt", "r").readlines()]

print(part1(input, preamble = 25)[1])
print(part2(input, preamble = 25))