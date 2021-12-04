import numpy as np

boards = []
nums = []
board = []
with open('day4_input.txt', 'r') as f:
    i = 0
    count = 0
    for line in f.readlines():
        if i == 0:
            nums = line.split(',')
            i += 1
            # print(line)
        else:
            # print('here')
            if line == '\n':
                if board:
                    boards.append(board)
                    board = []
                # print('boards', boards)

            else:
                row = line.strip('\n').split(' ')
                # print('row', row)
                row = [x for x in row if x]
                # print('clean row', row)
                board.append(row)
                # print('CURRENT BOARD', board)
        
        count += 1
        if count == 19:
            if board:
                    boards.append(board)
                    board = []


# np.array(boards)
# nrows = 5

# # print('boards', boards)
# boards = np.arange(5*5)
# boards = boards.reshape(5, 5)
# print('1st column', [row[0] for row in boards[0]])
# print('length', len(boards))

# HOW TO PRINT ROWS & COLUMNS
# print('1 row', boards[0][0])
# print('1 column', [row[0] for row in boards[0]])

# print('2 row', boards[0][1])
# print('2 column', [row[1] for row in boards[0]])

# a_board = boards[0]
# print('1st board', a_board)
# print('1 column', [row[0] for row in a_board])

def check_nums(one_rc):
    for num in one_rc:
        if int(num) > 0:
            return False
    return True

def got_bingo(a_board):
    # check rows
    for i in range(5):
        if check_nums(a_board[i]):
            return True

    # check cols
    for i in range(5):
        if check_nums(row[i] for row in a_board):
            return True

    return False

# print('bingo?', got_bingo(boards[0]))

# make the number a negative if it's marked
def cross_off(a_board, num):
    # print('the num', num)
    for i in range(5):
        for j in range(5):
            if int(a_board[i][j]) == int(num):
                # print('here')
                a_board[i][j] = -1

    return a_board

def find_sum(a_board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if int(a_board[i][j]) > 0:
                sum += int(a_board[i][j])
    
    return sum

# print('length', len(boards))
# test = boards[0]
# boards = [x for x in boards if x != test]
# print('new length', len(boards))

# ITERATING THROUGH BINGO NUMS
flag = False
for bingo_num in nums:
    # print('bingo num', bingo_num)
    for a_board in boards:
        # print('first board', a_board)
        a_board = cross_off(a_board, bingo_num) 
        # print('crossed off board', a_board)
        if got_bingo(a_board):
            if len(boards) == 1:
                winning_sum = find_sum(a_board)
                print('answer', winning_sum * int(bingo_num))
                flag = True
            else:
                boards = [x for x in boards if x != a_board]
            # winning_sum = find_sum(a_board)
            # print('sum', winning_sum)
            # print(winning_sum * int(bingo_num))
            
        if flag:
            break

    if flag:
        break



    
    