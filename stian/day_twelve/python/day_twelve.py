from requests.api import get
import time
import aoc_frame

def get_mapping(data) :
    mapping = {}
    for line in data :
        a, b = line.split('-')
        if a not in mapping :
            mapping[a] = []
        if b not in mapping :
            mapping[b] = []
        
        mapping[a].append(b)
        mapping[b].append(a)
    
    return mapping

def find_paths_one(i, mapping, curr_path) :
    if i == 'end' :
        return 1
    else :
        count = 0
        for j in mapping[i] :
            if (j == j.lower() and j not in curr_path) or j == j.upper() :
                curr_path.append(j)
                count += find_paths_one(j, mapping, curr_path)
                curr_path.pop()
    
    return count

def part_one(data) :
    mapping = {}
    for line in data :
        a, b = line.split('-')
        if a not in mapping :
            mapping[a] = []
        if b not in mapping :
            mapping[b] = []
        
        mapping[a].append(b)
        mapping[b].append(a)
    
    count = 0
    for i in mapping['start'] :
        count += find_paths_one(i, mapping, ['start', i])
    
    return count

def find_paths_two(i, mapping, curr_path, small) :
    if i == 'end' :
        return 1
    
    else :
        count = 0
        for j in mapping[i] :
            if j == 'start' :
                continue
            if (j == j.lower() and j in curr_path) and small == 0 :
                curr_path.append(j)
                count += find_paths_two(j, mapping, curr_path, 1)
                curr_path.pop()
            elif (j == j.lower() and j not in curr_path) or j == j.upper() :
                curr_path.append(j)
                count += find_paths_two(j, mapping, curr_path, small)
                curr_path.pop()
        
    return count


def part_two(data) :
    mapping = get_mapping(data)
    count = 0
    for i in mapping['start'] :
        count += find_paths_two(i, mapping, ['start', i], 0)
    
    return count

if __name__ == '__main__' :
    data = aoc_frame.get_data(2021, 12)
    test = aoc_frame.get_test_data(2021, 12)

    t0 = time.time()
    aoc_frame.format_strings(part_one(data), part_one(test), 1, t0)
    
    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test), 2, t0)