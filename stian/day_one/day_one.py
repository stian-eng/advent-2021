data = []

with open('day_one.txt', 'r') as f :
    for line in f.readlines() :
        data.append(line.strip('\n'))

print(data)