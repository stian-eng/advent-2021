from requests.api import get
import time
import aoc_frame

def part_one(data) :
    pass

def part_two(data) :
    pass

if __name__ == '__main__' :
    data = []
    test = []

    data2 = []
    test2 = []
    
    data = aoc_frame.get_data(2021, 9)
    test = aoc_frame.get_test_data(2021, 9)

    with open('day_twelve.txt', 'r') as f :
        for line in f.readlines() :
            data2.append(line.strip('\n'))
    
    with open('test.txt', 'r') as f :
        for line in f.readlines() :
            test2.append(line.strip('\n'))

    print(part_one(test2))
    print(part_one(data2))

    # t0 = time.time()
    # aoc_frame.format_strings(part_one(data, False), part_one(test, False), 1, t0)
    
    # t0 = time.time()
    # aoc_frame.format_strings(part_two(data), part_two(test), 2, t0)