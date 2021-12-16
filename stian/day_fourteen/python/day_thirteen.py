from requests.api import get
import time
import aoc_frame

def part_one(steps) :
    start = steps.pop(0)
    lookup = {}
    for i in range(len(steps)) :
        a, b = steps[i].replace(' ', '').split('->')
        lookup[a] = b
    
    counts = {}
    for i in range(10) :
        tmp = ''
        j = 0
        while j < len(start) - 1 :
            if start[j] + start[j + 1] in lookup :
                tmp += start[j] + lookup[start[j] + start[j + 1]]
            else :
                tmp += start[j]
            j += 1
        
        tmp += start[-1]
        start = tmp
    
    counts = {}
    for i in start :
        if i not in counts :
            counts[i] = 0
        
        counts[i] += 1
    
    max_count = 0
    min_count = float('inf')
    for i in counts :
        max_count = max(counts[i], max_count)
        min_count = min(counts[i], min_count)

    return max_count - min_count

def part_two(steps) :
    start = steps.pop(0)
    lookup = {}
    pairs = {}
    for i in range(len(steps)) :
        a, b = steps[i].replace(' ', '').split('->')
        lookup[a] = b
        pairs[a] = 0
    
    for i in range(len(start) - 1) :
        pair = start[i] + start[i + 1]
        if pair not in pairs :
            pairs[pair] = 0
        
        pairs[pair] += 1

    for i in range(40) :
        tmp = {}
        for p in pairs :
            if pairs[p] > 0 :
                pair_one = p[0] + lookup[p]
                pair_two = lookup[p] + p[1]
                if pair_one not in tmp :
                    tmp[pair_one] = 0
                if pair_two not in tmp :
                    tmp[pair_two] = 0
                
                tmp[pair_one] += pairs[p]
                tmp[pair_two] += pairs[p]
        
        for p in pairs :
            if p in tmp :
                pairs[p] = tmp[p]
            else :
                pairs[p] = 0
    
    counts = {}
    for p in pairs :
        j = p[0]
        if j not in counts :
            counts[j] = 0
        counts[j] += pairs[p]
    
    # adding in the very last letter lol
    counts[start[-1]] += 1

    return max(counts.values()) -  min(counts.values())

if __name__ == '__main__' :
    data = aoc_frame.get_data(2021, 14)
    test = aoc_frame.get_test_data(2021, 14)

    t0 = time.time()
    aoc_frame.format_strings(part_one(data), part_one(test), 1, t0)
    
    data = aoc_frame.get_data(2021, 14)
    test = aoc_frame.get_test_data(2021, 14)

    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test), 2, t0)