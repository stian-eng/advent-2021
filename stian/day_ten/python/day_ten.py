from requests.api import get
import time
import aoc_frame

def part_one(data,two) :
    """
    If a chunk opens with (, it must close with )
    If a chunk opens with [, it must close with ]
    If a chunk opens with {, it must close with }
    If a chunk opens with <, it must close with >
    """
    lookup = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}
    points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
    data2 = []
    # find the corrupted lines, where a chunk closes with the wrong character
    # some of the lines are not corrupted, just incomplete
    # find the first illegal character on each line, and look it up in the file
    total_points = 0
    stack = []
    for line in data :
        flag = True
        for i in line :
            if i not in lookup :
                stack.append(i)
            else :
                j = stack.pop()
                if j != lookup[i] :
                    flag = False
                    total_points += points[i]
                    break
        if flag :
            data2.append(line)
    
    if two :
        return data2
    
    return total_points

    pass

def part_two(data) :
    data = part_one(data, True)
    lookup = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
    points = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
    # multiply the total score by 5, and then add points
    all_points = []
    for line in data :
        stack = []
        point = 0
        for i in line :
            if i in lookup :
                stack.append(i)
            else :
                j = stack.pop()
        
        while stack :
            j = stack.pop()
            point *= 5
            point += points[lookup[j]]
        
        all_points.append(point)
    
    all_points.sort()
    return all_points[len(all_points) // 2]

if __name__ == '__main__' :
    data = []
    test = []

    data2 = []
    test2 = []
    
    data = aoc_frame.get_data(2021, 9)
    test = aoc_frame.get_test_data(2021, 9)

    with open('day_ten.txt', 'r') as f :
        for line in f.readlines() :
            data2.append(line.strip('\n'))
    
    with open('test.txt', 'r') as f :
        for line in f.readlines() :
            test2.append(line.strip('\n'))

    print(part_two(test2))
    print(part_two(data2))
    # t0 = time.time()
    # aoc_frame.format_strings(part_one(data), part_one(test2), 1, t0)
    
    # t0 = time.time()
    # aoc_frame.format_strings(part_two(data), part_two(test2), 2, t0)