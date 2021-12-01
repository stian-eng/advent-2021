data = []
data2 = []
with open('day_two.txt', 'r') as f :
    for line in f.readlines() :
        line = line.strip('\n').split(':')
        data.append(line[0])
        data2.append(line[1])

"""
part 1
"""
count = 0
for i in range(len(data)) :
    lower, upper = data[i].split('-')
    upper = upper.split()
    upper, letter = upper[0], upper[1]
    lower, upper = int(lower), int(upper)
    eval_string = data2[i]
    if lower <= eval_string.count(letter) <= upper :
        count += 1

"""
part 2
"""
count = 0
for i in range(len(data)) :
    tmp = 0
    lower, upper = data[i].split('-')
    upper = upper.split()
    upper, letter = upper[0], upper[1]
    lower, upper = int(lower), int(upper)
    eval_string = data2[i].strip()
    if eval_string[lower - 1] == letter :
        tmp += 1
    if eval_string[upper - 1] == letter :
        tmp += 1
    
    if tmp == 1 :
        count += 1
print(count)