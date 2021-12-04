data = []
with open('day3_input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        # stuff = line.split(" ")
        data.append(line)
        # data.append((line.strip('\n')))

# print(data)

length = 12

untouched_data = data
ones = {}
zeros = {}

for k in range(length):
    ones[k] = 0
    zeros[k] = 0

# print(int(data[0][0]))

def count(ones, zeros, new_data):
    for i in range(len(data)):
        for j in range(length):
            if int(data[i][j]) == 0:
                zeros[j] += 1
            else:
                ones[j] += 1

count(ones, zeros, data)

# print('ones', ones)
# print('zeros', zeros)


# o2: 0
# co2:



# print(ones)

# most = ''

# for l in range(5):
#     if ones[l] > zeros[l]:
#         most += '1'
#     else:
#         most += '0'

#941 * 3154
# print(most)

# pt 2

# def filter(stuff):
#     return [n for n in stuff if ]

# data = [k for k in data if k[0] == '0']
# print(data)

count(ones, zeros, data)

# print(ones)
# print(zeros)


for p in range(length):
    if ones[p] >= zeros[p]:
        data = data = [k for k in data if k[p] == '1']
        # print('1')
    else:
        data = data = [k for k in data if k[p] == '0']
        # print('0')

    ones = {}
    zeros = {}

    for k in range(length):
        ones[k] = 0
        zeros[k] = 0
    count(ones, zeros, data)

    # if p == 9:
    #     print('o2', data)

print('FIRST ONE', data)

data = untouched_data
count(ones, zeros, data)
# print('ones', ones)
# print('zeros', zeros)
# print('data', data)
for p in range(length):
    if zeros[p] < ones[p]:
        data = data = [k for k in data if k[p] == '0']
        # print('0')

    elif zeros[p] == ones[p]:
        data = data = [k for k in data if k[p] == '0']
        # print('0')
    else:
        data = data = [k for k in data if k[p] == '1']
        # print('1')

    if len(data) == 1:
        break

    # if p == length - 1:
    #     print('co2', data)
    ones = {}
    zeros = {}

    for k in range(length):
        ones[k] = 0
        zeros[k] = 0
    count(ones, zeros, data)


print('co2', data)

# print(ones, zeros)

# print(data)

2045, 3584



