from requests.api import get
import time
import aoc_frame

def part_one(data, flag) :
    lookup = {'0' : '0000', '1' : '0001', '2' : '0010','3' : '0011','4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}

    packet = ''
    for i in data :
        packet += lookup[i]
    i = 0
    if flag :
        return packet

    return parse_packet(packet, 1)[0]

def parse_four(packet) :
    binary_num = ''
    i = 0
    while i < len(packet):
        if packet[i] == '0' :
            binary_num += packet[i + 1 : i + 5]
            i += 5
            return binary_num, i
        else :
            binary_num += packet[i + 1 : i + 5]
            i += 5

def parse_packet(packet, part) :
    i = 0
    curr_version = int(packet[i : i + 3], 2)
    curr_type_id = int(packet[i + 3 : i + 6], 2)
    i += 6
    part_one = curr_version
    part_two = []
    sum = []
    if curr_type_id == 4 :
        # base case
        num, new_i = parse_four(packet[i:])
        i += new_i
        if part == 1 :
            return part_one, i
        else :
            return int(num, 2), i
    else :
        length_type_id = packet[i]
        i += 1
        if length_type_id == '1' :
            num_sub_packets = int(packet[i : i + 11], 2)
            i += 11
            for j in range(num_sub_packets) :
                val, new_i = parse_packet(packet[i:], part)
                i += new_i
                part_one += val
                part_two.append(val)
                sum.append(val)
            
        elif length_type_id == '0' :
            len_sub_packets = int(packet[i : i + 15], 2)
            i += 15
            j = i + len_sub_packets
            while i < j :
                val, new_i = parse_packet(packet[i:], part)
                i += new_i
                part_one += val
                part_two.append(val)
                sum.append(val)

    if part == 2 :
        return get_val(sum, curr_type_id), i
    elif part == 1 :
        return part_one, i

def get_val(nums, curr_type) :
    if curr_type == 0 :
        return sum(nums)
    elif curr_type == 1 :
        val = 1
        for i in nums :
            val *= i
        return val
    elif curr_type == 2 :
        return min(nums)
    elif curr_type == 3 :
        return max(nums)
    elif curr_type == 5 :
        if nums[0] > nums[1] :
            return 1
        return 0
    elif curr_type == 6 :
        if nums[0] < nums[1] :
            return 1
        return 0
    elif curr_type == 7 :
        if nums[0] == nums[1] :
            return 1
        return 0

def part_two(data) :
    packet = part_one(data, True)
    return parse_packet(packet, 2)[0]

if __name__ == '__main__' :
    data = []
    test = []
    with open('test.txt', 'r') as f :
        for line in f.readlines() :
            test.append(line.strip('\n'))
    
    with open('day_sixteen.txt', 'r') as f :
        for line in f.readlines() :
            data.append(line.strip('\n'))

    test = test[0]
    data = data[0]

    t0 = time.time()
    aoc_frame.format_strings(part_one(data, False), part_one(test, False), 1, t0)

    t0 = time.time()
    aoc_frame.format_strings(part_two(data), part_two(test), 2, t0)