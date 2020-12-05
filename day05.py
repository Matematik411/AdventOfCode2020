def binary_search(i, j, dir):
    if j-i==1:
        return [i, j][dir]
    
    if dir == 0:
        return [i, (i+j)//2]
    else:
        return [(i+j)//2 + 1, j]

sign_row = ["F", "B"]
sign_seat = ["L", "R"]

airplane = [[0 for _ in range(8)] for _ in range(128)]

max_id = 0
while True:
    try:
        data = input()
    except:
        break

    row = [0, 127]
    for x in data[0:7]:
        row = binary_search(row[0], row[1], sign_row.index(x))

    seat = [0, 7]
    for x in data[7:]:
        seat = binary_search(seat[0], seat[1], sign_seat.index(x))

    max_id = max(max_id, row*8 + seat)
    airplane[row][seat] = 1

print(airplane)
print(max_id)

count = 10
for row in airplane[10:]:
    if 0 in row:
        print(count*8 + row.index(0))
        break
    count += 1