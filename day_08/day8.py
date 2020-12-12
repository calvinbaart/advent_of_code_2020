import copy

class Processor:
    def __init__(self, memory):
        self.memory = memory
        self.accumulator = 0
        self.pc = 0

    def tick(self):
        instruction, arguments = self.memory[self.pc]
        self.pc += 1

        instruction_method = "instr_%s" % instruction

        if instruction_method in dir(self):
            getattr(self, instruction_method)(arguments)
        else:
            print("unknown instruction: %s" % instruction)

    def instr_nop(self, arguments):
        pass

    def instr_acc(self, arguments):
        num = int(arguments)
        
        self.accumulator += num

    def instr_jmp(self, arguments):
        location = int(arguments) - 1

        self.pc = self.pc + location


def part1(input):
    processor = Processor([x.split(" ", 1) for x in input])
    called = []

    while True:
        if processor.pc in called:
            return processor.accumulator
        
        called.append(processor.pc)
        processor.tick()

def part2(input):
    memory = [x.split(" ", 1) for x in input]
    current = -1

    while True:
        memory_copy = copy.deepcopy(memory)

        if current + 1 >= len(memory_copy):
            return -1

        for x in range(current + 1, len(memory_copy)):
            value = int(memory_copy[x][1])

            if value == 0:
                continue

            if memory_copy[x][0] == "jmp":
                memory_copy[x][0] = "nop"
                current = x
                break

            if memory_copy[x][0] == "nop":
                memory_copy[x][0] = "jmp"
                current = x
                break

        if current >= len(memory_copy):
            return -1

        processor = Processor(memory_copy)
        called = []
        failed = False

        while processor.pc < len(processor.memory):
            if processor.pc in called:
                failed = True
                break

            called.append(processor.pc)
            processor.tick()
        
        if failed is False:
            return processor.accumulator

input = [x.rstrip("\n") for x in open("input.txt", "r").readlines()]

print(part1(input))
print(part2(input))