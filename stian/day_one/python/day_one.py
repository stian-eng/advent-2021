data = []
test_data = []
with open('day_one.txt', 'r') as f :
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
    prev = data[0]
    count = 0
    for i in data[1:] :
        if i > prev :
            count += 1
    
    return count


def part_two(data) :
    prev_sum = 0
    curr_sum = 0
    count = 0
    for i in range(len(data)) :
        curr_sum += data[i]
        if i > 2 :
            if curr_sum > prev_sum :
                count += 1
            prev_sum = curr_sum
            curr_sum -= data[i - 2]
        
    return count

if __name__ == '__main__' :
    print("part 1:", part_one(data))
    print("part 1 TEST:", part_one(test_data))
    print("part 2:", part_two(data))
    print("part 2 TEST:", part_two(test_data))