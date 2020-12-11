#game of life
world = []
line = input()
w = len(line) + 2
world.append(["."for _ in range(w)])
world.append(["."]+list(line)+["."])
while True:
    try:
        line = input()
        world.append(["."]+list(line)+["."])
    except:
        break
world.append(["."for _ in range(w)])
h = len(world)

#vse skupaj obrnem, da lažje opazujem spreminjanje
world = [[world[i][j] for i in range(h)] for j in range(w)]
h, w = w, h
# ---------------
dirs = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]

#kopija za part two
original = [[elt for elt in line] for line in world]

#part one
change = True
nr_occupied = 0

while change:
    new = [[elt for elt in line] for line in world]
    print([''.join([str(elem) for elem in line]) for line in world])
    change = False
    for y, line in enumerate(world):
        if y in [0, h-1]:
            pass
        else:
            for x, organism in enumerate(line):
                if x in [0, w-1]:
                    pass
                else:
                    neighbors = 0
                    for path in dirs:
                        if world[y+path[1]][x+path[0]] == "#":
                            neighbors += 1
                    if neighbors == 0 and world[y][x] == "L":
                        new[y][x] = "#"
                        change = True
                        nr_occupied += 1
                    if neighbors >= 4 and world[y][x] == "#":
                        new[y][x] = "L"
                        change = True
                        nr_occupied -= 1
    world = [[elt for elt in line] for line in new]




print([''.join([str(elem) for elem in line]) for line in world])
print(nr_occupied)


#part two
world = [[elt for elt in line] for line in original]


change = True 
nr2 = 0

while change:
    new = [[elt for elt in line] for line in world]
    print([''.join([str(elem) for elem in line]) for line in world])
    change = False
    for y, line in enumerate(world):
        if y in [0, h-1]:
            pass
        else:
            for x, organism in enumerate(line):
                if x in [0, w-1]:
                    pass
                else:
                    neighbors = 0
                    for path in dirs:
                        k = 0
                        while True:
                            k += 1
                            try:
                                if world[y+path[1]*k][x+path[0]*k] == "L" or (y+path[1]*k)*(x+path[0]*k) <= 0:
                                    break
                                elif world[y+path[1]*k][x+path[0]*k] == "#":
                                    neighbors += 1
                                    break
                            except:
                                break
                    if (x, y) == (1, 1):
                        print(neighbors)
                    if neighbors == 0 and world[y][x] == "L":
                        new[y][x] = "#"
                        change = True
                        nr2 += 1
                    if neighbors >= 5 and world[y][x] == "#":
                        new[y][x] = "L"
                        change = True
                        nr2 -= 1
    world = [[elt for elt in line] for line in new]

print([''.join([str(elem) for elem in line]) for line in world])
print(nr_occupied, nr2)