# first half
with open('/Users/student/Desktop/Advent of Code/Day2.txt') as f:
    total = 0
    lines = f.readlines()
    rps = {'X': 1, 'Y': 2, 'Z': 3}
    for line in lines:
        total += int(rps[line.split(' ')[1].split('\n')[0]])
    for line in lines:
        opponent = line.split(' ')[0]
        myself = line.split(' ')[1].split('\n')[0]
        result = ord(myself) - ord(opponent)
        if result == 24 or result == 21:
            total += 6
        elif result == 23:
            total += 3
        else:
            continue
    print(total)

# second half
with open('/Users/student/Desktop/Advent of Code/Day2.txt') as f:
    total = 0
    lines = f.readlines()
    rps = {'X': 0, 'Y': 3, 'Z': 6}
    for line in lines:
        total += int(rps[line.split(' ')[1].split('\n')[0]])
    rps2 = {'A': [1, 2, 3], 'B': [2, 3, 1], 'C': [3, 1, 2]}
    determine = {'X': 2, 'Y': 0, 'Z': 1}
    for line in lines:
        determin = line.split(' ')[1].split('\n')[0]
        opponent = line.split(' ')[0]
        number = determine[determin]
        total += rps2[opponent][number]
    print(total)
