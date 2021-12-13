from requests.api import get
import time
import aoc_frame

def get_points(data) :
    points = []
    instr = []
    flag = True
    for i in data :
        if i :
            if flag :
                x, y = i.split(',')
                points.append((int(x), int(y)))
            else :
                y = i.split()
                x = y[-1]
                axis, num = x.split('=')
                instr.append((axis, int(num)))
        else :
            flag = False

    return points, instr


def fold(points, fold) :
    if fold[0] == 'y' :
            for i in range(len(points)) :
                curr = points[i]
                if curr[1] > fold[1] :
                    points[i] = (curr[0], fold[1] - (curr[1] - fold[1]))
        
    elif fold[0] == 'x' :
        for i in range(len(points)) :
            curr = points[i]
            if curr[0] > fold[1] :
                points[i] = (fold[1] - (curr[0] - fold[1]), curr[1])
    
    return points

def part_one(data, flag2) :
    points, instr = get_points(data)

    for f in instr :
        points = fold(points, f)
        if flag2 :
            seen = set()
            count = 0
            for i in points :
                if i not in seen :
                    seen.add(i)
                    count += 1
        
            return count
    
    return points


def part_two(data) :
    points = part_one(data, False)
    max_x = max([i[0] for i in points])
    max_y = max([i[1] for i in points])
    matrix = [[' ' for i in range(max_x + 1)] for i in range(max_y + 1)]
    seen = set()
    for p in points :
        if p not in seen :
            matrix[p[1]][p[0]] = '#'
            seen.add(p)
    for i in matrix :
        print(i)

    # answer:
    """
    [[' ', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'], 
     ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'], 
     ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', '#', '#'], 
     ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'], 
     ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'], 
     ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', '#']]
    """

if __name__ == '__main__' :
    data = []
    test = []

    with open('day_thirteen.txt', 'r') as f :
        for line in f.readlines() :
            data.append(line.strip('\n'))
    
    with open('test.txt', 'r') as f :
        for line in f.readlines() :
            test.append(line.strip('\n'))

    t0 = time.time()
    aoc_frame.format_strings(part_one(data, True), part_one(test, True), 1, t0)
    
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test), 2, t0)