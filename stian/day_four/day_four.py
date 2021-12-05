import aoc_frame
import copy

def part_one(data) :
    # calculate which board will win first
    # print(data)
    numbers = data[0][0][0]
    winners = []
    del data[0]
    winning_nums = {}
    for k, n in enumerate(numbers.split(',')):
        if set(winning_nums.keys()) == set(data.keys()) :
            break
        # if len(winners) == len(data) :
        #     break
        mark_numbers(data, n)
        
        for k in data :
            board = data[k]
            if has_horizontal(board) :
                # first winner
                if k not in winners :
                    winners.append(k)
                    winning_nums[k] = n

            if has_vertical(board) :
                if k not in winners :
                    winners.append(k)
                    winning_nums[k] = n

    last_winner = winners[-1]
    return calculate_score(data[last_winner], winning_nums[last_winner])

def calculate_score(board, num) :
    print(board, num)
    sum = 0
    for i in board :
        for j in i :
            if j != '-1' :
                sum += int(j)
    print(sum, num)
    return sum * int(num)

def mark_numbers(data, num) :
    for k in data :
        board = data[k]
        for i in range(len(board)) :
            for j in range(len(board[i])) :
                if board[i][j] == num :
                    board[i][j] = '-1'
    
    return data


def has_horizontal(board) :
    for row in board :
        for i in row :
            flag = True
            if i != '-1' :
                flag = False
                break
        if flag :
            return True
    
    return False

def has_vertical(board) :
    k = 0
    for i in range(len(board[0])) :
        flag = True
        for j in range(len(board)) :
            if board[j][k] != '-1' :
                flag = False
                break
        k += 1
        if flag :
            return True
    
    return False

def part_two(data) :                
    pass

def helper(data) :
    pass

if __name__ == '__main__' :
    data = []
    test_data = []
    # data, test_data = aoc_frame.read_data(2021, 4)
    with open('day_four.txt', 'r') as f :
        for line in f.readlines() :
            board = []
            if line != '\n' :
                board.append(line.strip('\n').split())
            else :
                data.append(board)
                board = []
    # part_one(data)
    with open('day_four.txt', 'r') as f :
        # test = f.read().split('\n')

        # for i in range(len(test)) :
        #     if i == 0 :
        #         nums = i
        #     elif not test[i] :
        #         # part of curr board
        boards = {}
        i = 0
        boards[i] = []
        for line in f.readlines() :
            if line != '\n' :
                boards[i].append(line.split())
            else :
                i += 1
                boards[i] = []
    # print(test_data)
    print(part_one(boards))

    # mark_numbers(test_data, '11')
    # print(test_data)
    # print(data)
    # print('Test Data:', test_data, '\n')
    # aoc_frame.format_strings(part_one(data), part_one(test_data), 1)
    # aoc_frame.format_strings(part_two(data), part_two(test_data), 2)