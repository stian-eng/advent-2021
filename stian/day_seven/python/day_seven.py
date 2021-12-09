from requests.api import get
import time
import aoc_frame

storage = {}

def part_one(data) :
    data = data[0].split(',')
    data = [int(i) for i in data]
    diff = 0
    min_diff = float('inf')
    for i in range(max(data)) :
        diff = 0
        for j in data :
            diff += abs(i - j)

        min_diff = min(diff, min_diff)
    
    return min_diff


def calc_fuel(i, num) :
    # the distance between two points only needs to be calculated once
    # n (n + 1) / 2
    n = abs(num - i)
    return (n * (n + 1)) // 2

def part_two(data) :  
    data = data[0].split(',')
    data = [int(i) for i in data]
    diff = 0
    min_diff = float('inf')
    for i in range(max(data)) :
        diff = 0
        for j in data :
            diff += calc_fuel(j, i)

        min_diff = min(diff, min_diff)
    
    return min_diff

if __name__ == '__main__' :
    data = aoc_frame.get_data(2021, 7)
    test_data = aoc_frame.get_test_data(2021, 7)
    if data[0] == 'didnt work :/' :
        with open('day_seven.txt', 'r') as f :
            for line in f.readlines() :
                data.append(line.strip('\n'))
    
    if test_data[0] == 'didnt work :/' :
        with open('test.txt', 'r') as f :
            for line in f.readlines() :
                test_data.append(line.strip('\n'))

    t0 = time.time()
    aoc_frame.format_strings(part_one(data), part_one(test_data), 1, t0)
    
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test_data), 2, t0)
    