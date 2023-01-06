# part1
with open('/Users/student/Desktop/Advent of Code/Day4.txt') as f:
    count = 0
    lines = f.readlines()
    for line in lines:
        a, b = line.split(', ')
        first = a.split('-')
        second = b.split('-')
        if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1])):
            count += 1
    print(count)

# part2
with open('/Users/student/Desktop/Advent of Code/Day4.txt') as f:
    count = 0
    lines = f.readlines()
    for line in lines:
        a, b = line.split(', ')
        first = a.split('-')
        second = b.split('-')
        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1]):
            count += 1
        if int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[0]) and int(second[1]) <= int(first[1]):
            count += 1
    print(count)
