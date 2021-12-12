from requests.api import get
import time
import aoc_frame

def part_one(data) :
    d = []
    count = 0
    look_for = [2, 4, 3, 7]
    for i in data :
        j = i.split('|')
        d.append(j[1].strip())
        # for k, v in enumerate(j[0].split()) :
        #     if k in [1, 4, 7, 8] :
        #         look_for.append(len(v))
        for k in j[1].strip().split() :
            if len(k) in look_for :
                count += 1
    
    return count

def part_two(data) :
    look_for = [2, 4, 3, 7]
    other_mappings = {2 : '1', 4 : '4', 3 : '7', 7 : '8'}
    mappings_one = {1 : '256', 2 : '039'}
    mappings_four = {3 : '0356', 2 : '2', 4 : '9'}
    mappings_seven = {3 : '039', 2 : '256'}
    mappings_eight = {6 : '069', 5 : '235'}
    sum = 0
    for i in data :
        l = i.split('|')
        curr_mapping = {}
        num = ''
        for j in l[0].strip().split() :
            if len(j) in look_for :
                curr_mapping[other_mappings[len(j)]] = j
        for j in l[1].strip().split() :
            could_be = ''
            if len(j) in other_mappings :
                num += other_mappings[len(j)]
            else :
                for i in curr_mapping :
                    v = curr_mapping[i]
                    if i == '1' :
                        could_be = find_common(mappings_one[get_overlap(v, j)], could_be)
                    elif i == '4' :
                        could_be = find_common(mappings_four[get_overlap(v, j)], could_be)
                    elif i == '7' :
                        could_be = find_common(mappings_seven[get_overlap(v, j)], could_be)
                    elif i == '8' :
                        could_be = find_common(mappings_eight[get_overlap(v, j)], could_be)
                    if len(could_be) == 1 :
                        break
                
                num += could_be
        sum += int(num)

    return sum

def find_common(a, b) :
    if not a or not b :
        if not a :
            return b
        else :
            return a

    c = ''
    for i in a :
        if i in b :
            c += i

    return c          

def get_overlap(a, b) :
    count = 0
    for i in a :
        if i in b :
            count += 1
    
    return count

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