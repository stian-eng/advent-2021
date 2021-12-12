from requests.api import get
import time
import aoc_frame

def part_one(data, flag) :
    new_data = []
    for i in range(len(data)) :
        new_data.append([int(j) for j in data[i]])
    
    if flag :
        return new_data

    i = 0
    flashes = 1
    while i < 100 :
        energy_level(new_data)
        seen = flash(new_data)
        flashes += len(seen)
        for coord in seen :
            new_data[coord[0]][coord[1]] = 0
        
        i +=  1
    
    return flashes

def energy_level(data) :
    for i in range(len(data)) :
        for j in range(len(data[i])) :
            data[i][j] += 1

def flash(data) :
    seen = set()
    flag = True
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    while flag :
        flag = False
        for i in range(len(data)) :
            for j in range(len(data[i])) :
                if data[i][j] > 9 and (i, j) not in seen :
                    flag = True
                    # every time there is a flash we add it to seen
                    seen.add((i, j))
                    for d in dirs :
                        n = (i + d[0], j + d[1])
                        if 0 <= n[0] < len(data) and 0 <= n[1] < len(data[n[0]]) :
                            data[n[0]][n[1]] += 1
    
    return seen


def part_two(data) :
    data = part_one(data, True)
    day = 1
    while True :
        energy_level(data)
        seen = flash(data)
        for coord in seen :
            data[coord[0]][coord[1]] = 0

        if len(seen) == (len(data) * len(data[0])) :
            return day
        
        day += 1

if __name__ == '__main__' :
    data = []
    test = []
    
    data = aoc_frame.get_data(2021, 11)
    test = aoc_frame.get_test_data(2021, 11)

    t0 = time.time()
    aoc_frame.format_strings(part_one(data, False), part_one(test, False), 1, t0)
    
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test), 2, t0)