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
    final_list = []
    lines = f.readlines()
    print(len(lines))

    for i in range(0, len(lines), 3):
        first_dict = {}
        second_dict = {}
        third_dict = {}
        for key in lines[i]:
            first_dict[key] = 0
        for value in lines[i+1]:
            if value in first_dict:
                second_dict[value] = 0
        for value in lines[i+2]:
            if value in second_dict:
                third_dict[value] = 0
        for value in third_dict:
            final_list.append(value)
    for value in final_list:
        if ord(value) >= 97 and ord(value) <= 122:
            total += ord(value)-96
        elif ord(value) >= 65 and ord(value) <= 90:
            total += ord(value)-38
    print(total)
