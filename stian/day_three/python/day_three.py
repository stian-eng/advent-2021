import aoc_frame

def part_one(data, flag) :
    count_zero = [0 for i in range(len(data[0]))]
    count_one = [0 for i in range(len(data[0]))]
    for i in data :
        for k, v in enumerate(i) :
            if v == '1' :
                count_one[k] += 1
            else :
                count_zero[k] += 1
    
    gamma = ''
    epsilon = ''
    for i in range(len(count_zero)) :
        if count_zero[i] > count_one[i] :
            gamma += '0'
            epsilon += '1'
        elif count_zero[i] < count_one[i] :
            gamma += '1'
            epsilon += '0'
        else :
            gamma += '1'
            epsilon += '0'
    
    if flag :
        return gamma, epsilon

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

def part_two(data) :                
    gamma, epsilon = part_one(data, True)
    kept = data
    i = 0
    while len(kept) > 1 :
        gamma, epsilon = part_one(kept, True)
        kept = find_remaining(kept, gamma, i)
        i += 1
    oxygen = int(kept[0], 2)
    
    kept = data
    i = 0
    while len(kept) > 1 :
        gamma, epsilon = part_one(kept, True)
        kept = find_remaining(kept, epsilon, i)
        i += 1
    
    carbon = int(kept[0], 2)

    return oxygen * carbon

def find_remaining(data, keyword, index) :
    new_data = []
    for i in data :
        if i[index] == keyword[index] :
            new_data.append(i)
    
    return new_data

if __name__ == '__main__' :
    data = []
    test_data = []

    data, test_data = aoc_frame.read_data(2021, 3)
    print('Test Data:', test_data, '\n')
    aoc_frame.format_strings(part_one(data, False), part_one(test_data, False), 1)
    aoc_frame.format_strings(part_two(data), part_two(test_data), 2)