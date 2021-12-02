data = []
test_data = []
with open('day_two.txt', 'r') as f :
    for line in f.readlines() :
        data.append(line.strip('\n'))

with open("test.txt", 'r') as f :
    for line in f.readlines() :
        test_data.append(line.strip('\n'))

# GUT CHECK
print(test_data, len(test_data))
print(data[0], data[1], data[-1], len(data))

def part_one(data) :
    horizontal = 0
    depth = 0
    for i in data :
        direction, num = i.split()
        if direction == 'forward' :
            horizontal += int(num)
        elif direction == 'up' :
            depth -= int(num)
        else :
            depth += int(num)
        
    return horizontal * depth

def part_two(data) :
    horizontal = 0
    depth = 0
    aim  = 0
    for i in data :
        direction, num = i.split()
        if direction == 'forward' :
            horizontal += int(num)
            depth += aim * int(num)
        elif direction == 'up' :
            aim -= int(num)
        else :
            aim += int(num)
        
    return horizontal * depth

if __name__ == '__main__' :
    print("PART 1:", part_one(data))
    print("PART 1 TEST INPUT:", part_one(test_data))
    print("PART 2:", part_two(data))
    print("PART 2 TEST:", part_two(test_data))