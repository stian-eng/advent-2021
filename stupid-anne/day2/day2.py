data = []
with open('day2_input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        stuff = line.split(" ")
        data.append(stuff)
        # data.append((line.strip('\n')))


horizontal = 0
depth = 1
aim = 0


for thing in data:
    if thing[0] == 'forward':
        horizontal += int(thing[1])
        depth += aim * int(thing[1])
    elif thing[0] == 'down':
        aim += int(thing[1])
    elif thing[0] == 'up':
        aim -= int(thing[1])

print(horizontal * (depth - 1))
print(horizontal)
print(depth)