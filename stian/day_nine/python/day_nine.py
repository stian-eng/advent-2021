from requests.api import get
import time
import aoc_frame

def part_one(data) :
    pass

def part_two(data) :
    pass

if __name__ == '__main__' :
    data = []
    test_data = []
    with open('day_seven.txt', 'r') as f :
        for line in f.readlines() :
            data.append(line.strip('\n'))
    
    with open('test.txt', 'r') as f :
        for line in f.readlines() :
            test_data.append(line.strip('\n'))

    t0 = time.time()
    aoc_frame.format_strings(part_one(data), part_one(test_data), 1, t0)
    
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test_data), 2, t0)