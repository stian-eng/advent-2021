import aoc_frame

def part_one(data) :
    pass

def part_two(data) :                
    pass

def helper(data) :
    pass

if __name__ == '__main__' :
    data = []
    test_data = []

    data, test_data = aoc_frame.read_data(2021, 3)
    print('Test Data:', test_data, '\n')
    aoc_frame.format_strings(part_one(data), part_one(test_data), 1)
    aoc_frame.format_strings(part_two(data), part_two(test_data), 2)