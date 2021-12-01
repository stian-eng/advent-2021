data = []
test_data = []
with open('day_two.txt', 'r') as f :
    for line in f.readlines() :
        # CASTING AS INT MAYBE THATS THE PROB??
        data.append(int(line.strip('\n')))

with open("test.txt", 'r') as f :
    for line in f.readlines() :
        test_data.append(int(line.strip('\n')))

# GUT CHECK
print(test_data, len(test_data))
print(data[0], data[1], data[-1], len(data))

def part_one(data) :
    pass


def part_two(data) :
    pass

if __name__ == '__main__' :
    print("part 1:", part_one(data))
    print("part 1 TEST:", part_one(test_data))
    print("part 2:", part_two(data))
    print("part 2 TEST:", part_two(test_data))