# 1st part
pos = [0, 0]
angle = 0

sides = ["E", "N", "W", "S"]
meaning = {"N":[0, 1], "S": [0, -1], "E":[1, 0], "W":[-1, 0]}

# 2nd part
position = [0, 0]
waypoint = [10, 1]

def rotate(way, direction):
    if direction > 0:
        for _ in range(direction):
            way = [-way[1], way[0]]
    else:
        for _ in range(-direction):
            way = [way[1], -way[0]]
    return way




# 1st part --- 2nd part 

while True:
    try:
        a = input()
        if a[0] in sides:
            pos[0] += meaning[a[0]][0]*int(a[1:])
            pos[1] += meaning[a[0]][1]*int(a[1:])
            # ---
            waypoint[0] += meaning[a[0]][0]*int(a[1:])
            waypoint[1] += meaning[a[0]][1]*int(a[1:])

        elif a[0] == "F":
            pos[0] += meaning[sides[angle]][0]*int(a[1:])
            pos[1] += meaning[sides[angle]][1]*int(a[1:])
            # ---
            position[0] += waypoint[0]*int(a[1:])
            position[1] += waypoint[1]*int(a[1:])

        elif a[0] == "L":
            angle += int(a[1:])//90
            angle %= 4
            # ---
            waypoint = rotate(waypoint, int(a[1:])//90)

        elif a[0] == "R":
            angle -= int(a[1:])//90
            angle %= 4
            # ---
            waypoint = rotate(waypoint, -int(a[1:])//90)
        
    except:
        break


print(pos, abs(pos[0]) + abs(pos[1]))
print(position, abs(position[0]) + abs(position[1]))