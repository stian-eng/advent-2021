from requests.api import get
import time
import aoc_frame

def part_one(data) :
    data2 = []
    for i in data :
        tmp = []
        for j in i :
            tmp.append(int(j))
        data2.append([x for x in tmp])

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    sum = 0
    for i in range(len(data2)) :
        for j in range(len(data2[i])) :
            curr = data2[i][j]
            flag = True
            for d in dirs :
                n = (i + d[0], j + d[1])
                if 0 <= n[0] < len(data2) and 0 <= n[1] < len(data2[i]) :
                    if data2[n[0]][n[1]] <= curr :
                        flag = False
            if flag :
                sum += curr + 1
    
    return sum

def part_two(data) :
    # 9 is never in a basin
    data2 = []
    for i in data :
        tmp = []
        for j in i :
            tmp.append(int(j))
        data2.append([x for x in tmp])
    sizes = []
    for i in range(len(data2)) :
        for j in range(len(data2[i])) :
            if data2[i][j] != 9 :
                z = bfs(data2, i, j)
                sizes.append(z)

    sizes.sort(reverse = True)
    total = 1
    i = 0
    while i < 3 :
        total *= sizes[i]
        i += 1
    
    return total

def bfs(data, i, j) :
    # when we reach a low point, we will use that basin num
    # then we will assign that to every point that goes into that basin
    # if we run into a basin num that we know (we wil actually use a letter)
    # then we automatically assign all seen to that basin
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [(i, j)]
    seen = set()
    seen.add((i, j))
    while queue :
        curr = queue.pop(0)
        for d in dirs :
            n = (curr[0] + d[0], curr[1] + d[1])
            if 0 <= n[0] < len(data) and 0 <= n[1] < len(data[i]) :
                if data[n[0]][n[1]] != 9 and n not in seen :
                    seen.add(n)
                    queue.append(n)
    
    for coord in seen :
        data[coord[0]][coord[1]] = 9
    
    return len(seen)

if __name__ == '__main__' :
    data = []
    test = []

    data2 = []
    test2 = []
    
    data = aoc_frame.get_data(2021, 9)
    test = aoc_frame.get_test_data(2021, 9)

    with open('day_nine.txt', 'r') as f :
        for line in f.readlines() :
            data2.append(line.strip('\n'))
    
    with open('test.txt', 'r') as f :
        for line in f.readlines() :
            test2.append(line.strip('\n'))

    # print(part_two(test2))
    # print(part_two(data2))
    t0 = time.time()
    aoc_frame.format_strings(part_one(data), part_one(test2), 1, t0)
    
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test2), 2, t0)