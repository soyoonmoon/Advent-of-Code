# part1
final_list = []
with open('/Users/student/Desktop/Advent of Code/Day3.txt') as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        first = set(line[:(len(line)//2)])
        last = set(line[len(line)//2:])
        final_list.append(list(first - (first-last))[0])
    for value in final_list:
        if ord(value) >= 97 and ord(value) <= 122:
            total += ord(value)-96
        else:
            total += ord(value)-38
    print(total)

# part2
with open('/Users/student/Desktop/Advent of Code/Day3.txt') as f:
    total = 0
    lines = f.readlines()
    first_dict = {}
    second_dict = {}
    for i in range(0, len(lines), 3):
        first = set(lines[i])
        second = set(lines[i+1])
        third = dict(set(lines[i+2]))
        print(first)
        print(second)
        print(third)
