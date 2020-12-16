import re
#reads conditions
ranges = []
for _ in range(20):#20
    line = input()
    _, a, b, c, d, _ = re.split(r".* (\d+)-(\d+) or (\d+)-(\d+)", line)
    ranges.append([[int(a), int(b)], [int(c), int(d)]])

input()
input()
#reads my ticket
mine = list(map(int, input().split(",")))

input()
input()

#part one - sums up error_rate and only keeps valid tickets for part two
error_rate = 0
valids = []
for _ in range(243):#243
    ticket = list(map(int, input().split(",")))
    corrupted = False

    for value in ticket:
        found = False
        #print("valueeee", value)
        for data in ranges:
            if found:
                break

            if data[0][0] <= value <=data[0][1] or data[1][0] <= value <=data[1][1]:

                found = True
        if not found:
            corrupted = True
            error_rate += value
    
    if not corrupted:
        valids.append(ticket)

#creates remaining options for each field on the ticket
fields = []
for data in ranges:
    all_copy = []
    for data2 in ranges:
        copy = data2[0][::]
        copy2 = data2[1][::]
        all_copy.append([copy, copy2])
    fields.append(all_copy)

#checks which fields are not posible because of the data on the tickets
for ticket in valids:
    for i, value in enumerate(ticket):
        for j, data in enumerate(ranges):
            if (data[0][0] <= value <= data[0][1] or data[1][0] <= value <= data[1][1]):
                pass
            else:
                fields[i][j] = False

#by process of elimination determines which field on the ticket belongs to each condition
#true location is a list of these field locations
n = len(fields)
true_location = [0 for _ in range(n)]
while fields.count(False) < n:
    for j, data in enumerate(fields):
        if data == False:
            continue
        nr_falses = 0
        loc = 0
        for i, value in enumerate(data):
            if value == False:
                nr_falses += 1
            else:
                loc = i
        if nr_falses == n-1:
            true_location[loc] = j
            for update in fields:
                if update == False:
                    continue
                update[loc] = False
        elif nr_falses == n:
            fields[j] = False

#multiplies locations for the "depature" conditions
target = 1
for i in true_location[:6]:
    target *= mine[i]

#prints results for each part
print(error_rate)
print(target)