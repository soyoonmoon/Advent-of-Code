all_elves = []
with open('/Users/student/Desktop/Advent of Code/Day1.txt') as f:
    current = 0
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            all_elves.append(current)
            current = 0
        else:
            current += int(line)
    all_elves.sort(reverse=True)
    print(all_elves[0]+all_elves[1]+all_elves[2])
