data = []
test_data = []
with open('day_three.txt', 'r') as f :
    for line in f.readlines() :
        data.append(line.strip('\n'))

with open("test.txt", 'r') as f :
    for line in f.readlines() :
        test_data.append(line.strip('\n'))

# GUT CHECK
print(test_data, len(test_data))
print(data[0], data[1], data[-1], len(data))

def part_one(data) :
    pass

def part_two(data) :
    pass

if __name__ == '__main__' :
    print("PART 1:", part_one(data))
    print("PART 1 TEST INPUT:", part_one(test_data))
    print("PART 2:", part_two(data))
    print("PART 2 TEST:", part_two(test_data))