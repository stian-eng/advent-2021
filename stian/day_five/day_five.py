from requests.api import get
import aoc_frame

def part_one(data, flag) :
    lookup = {}
    part2 = []
    for i in data :
        p1, p2 = get_points(i)
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])
        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        if p1[0] == p2[0] :
            for i in range(min_y, max_y + 1) :
                if (int(p1[0]), i) not in lookup :
                    lookup[(p1[0], i)] = 0
                lookup[(p1[0], i)] += 1
        elif p1[1] == p2[1] :
            for i in range(min_x, max_x + 1) :
                if (i, p1[1]) not in lookup :
                    lookup[(i, p1[1])] = 0
                lookup[(i, p1[1])] += 1
        else :
            part2.append(i)
    
    if flag :
        return lookup, part2

    count = 0 
    for i in lookup :
        if lookup[i] > 1 :
            count += 1

    return count

def part_two(data) :                
    lookup, new_data = part_one(data, True)
    for i in new_data :
        p1, p2 = get_points(i)
        if p1[1] < p2[1] :
            num = 1
        else :
            num = -1
        x, y = p1[0], p1[1]
        while x <= p2[0] :
            if (x, y) not in lookup :
                lookup[(x, y)] = 0
            lookup[(x, y)] += 1
            x += 1
            y += num
    
    count = 0 
    for i in lookup :
        if lookup[i] > 1 :
            count += 1

    return count

def get_points(line) :
    # always return the lowest x point
    left, right = line.split('->')
    x1, y1 = left.strip().split(',')
    x2, y2 = right.strip().split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)

    if x1 > x2 :
        return (x2, y2), (x1, y1)

    return (x1, y1), (x2, y2)

if __name__ == '__main__' :
    data = aoc_frame.get_data(2021, 5)
    test_data = aoc_frame.get_test_data(2021, 5)
    aoc_frame.format_strings(part_one(data, False), part_one(test_data, False), 1)
    aoc_frame.format_strings(part_two(data), part_two(test_data), 2)
    