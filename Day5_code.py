def create_stacks(lines):
    num_stack = int(len(lines[6])/4)
    stacks = [[] for _ in range(num_stack)]

    for line in lines:
        for pos, i in enumerate(line):
            if i.isalpha():
                stacks[int((pos-1)/4)].append(i)
    # changing all the inputs in stack form
            if line[1] == "1":
                stacks = [i[::-1] for i in stacks]
                return(stacks)


def part1():
    with open('/Users/student/Desktop/Advent of Code/Day5.txt') as f:
        lines = f.readlines()
        stacks = create_stacks(lines)

        for line in lines[10:]:
            final = line.split(' ')
            num_to_move = int(final[1])
            from_stack = int(final[3])
            to_stack = int(final[5])
            for _ in range(num_to_move):
                current = stacks[from_stack-1].pop()
                stacks[to_stack-1].append(current)
        final = []
        for i in range(len(stacks)):
            final.append(stacks[i][-1])
        return final


print(part1())


def part2():
    with open('/Users/student/Desktop/Advent of Code/Day5.txt') as f:
        lines = f.readlines()
        stacks = create_stacks(lines)
        for line in lines[10:]:
            final = line.split(' ')
            num_to_move = int(final[1])
            from_stack = int(final[3])
            to_stack = int(final[5])
            for i in stacks[from_stack-1][-num_to_move:]:
                stacks[to_stack-1].append(i)
            stacks[from_stack-1] = stacks[from_stack -
                                          1][:len(stacks[from_stack-1])-(num_to_move)]
        final = []
        for i in range(len(stacks)):
            final.append(stacks[i][-1])
        return final


print(part2())
