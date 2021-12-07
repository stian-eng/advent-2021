from requests.api import get
import time
import aoc_frame

def part_one(data) :
    for i in range(80) :
        new_fish = 0
        for k, v in enumerate(data) :
            if v == 0 :
                data[k] = 6
                new_fish += 1
            else :
                data[k] -= 1
        
        for i in range(new_fish) :
            data.append(8)
    
    return len(data)

def part_two(data) :  
    counts = [0 for i in range(9)]
    for i in data :
        counts[i] += 1

    for i in range(256) :
        # take the # at zero and add it to 6, then add it to 8
        # everything else is decremented by one
        zeros = counts[0]
        for i in range(8) :
            counts[i] = counts[i + 1]
        counts[8] = 0
        counts[6] += zeros
        counts[8] += zeros
    
    return sum(counts)

if __name__ == '__main__' :
    data = aoc_frame.get_data(2021, 6)
    test_data = aoc_frame.get_test_data(2021, 6)
    data, test_data = data[0].split(','), test_data[0].split(',')
    data = [int(i) for i in data]
    test_data = [int(i) for i in test_data]
    t0 = time.time()
    aoc_frame.format_strings(part_one(data), part_one(test_data), 1)
    t1 = time.time()
    print('Part 1 completed in', round(t1 - t0, 5), 'seconds')
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test_data), 2)
    t1 = time.time()
    print('Part 2 completed in', round(t1 - t0, 5), 'seconds')
    