#3D game of life

world = {}
plane = []
line = input()
w = len(line) + 14
for _ in range(7):
    plane.append(["."for _ in range(w)])
    
plane.append(["."for _ in range(7)]+list(line)+["."for _ in range(7)])
while True:
    try:
        line = input()
        plane.append(["."for _ in range(7)]+list(line)+["."for _ in range(7)])
    except:
        break
for _ in range(7):
    plane.append(["."for _ in range(w)])
h = len(plane)
world[0] = plane

for i in range(-7, 8):
    if i != 0:
        plane = [["." for _ in range(w)] for _ in range(h)]
        world[i] = plane


dirs = []
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            if [x, y, z] != [0, 0, 0]:
                dirs.append([x, y, z])


#kopija za part two
galaxy = {}
for z in range(-7, 8):
    for WW in range(-7, 8):
        if (WW, z) == (0,0):
            original = [[elt for elt in line] for line in world[0]]
        else:
            original = [[elt for elt in line] for line in world[-1]]
        galaxy[(WW, z)] = original

#part one
nr_occupied = 29 # 29

for cycle in range(1, 7):
    new = {}
    for i in range(-7, 8):
        new_plane = [[elt for elt in line] for line in world[i]]
        new[i] = new_plane

    for z in range(-cycle, cycle+1):
        for y, line in enumerate(world[z]):
            if y in [0, h-1]:
                pass
            else:
                for x, organism in enumerate(line):
                    if x in [0, w-1]:
                        pass
                    else:
                        neighbors = 0
                        for path in dirs:
                            if world[z+path[2]][y+path[1]][x+path[0]] == "#":
                                neighbors += 1
                        
                        if neighbors == 3 and world[z][y][x] == ".":
                            new[z][y][x] = "#"
                            nr_occupied += 1
                        if neighbors != 2 and neighbors != 3 and world[z][y][x] == "#":
                            new[z][y][x] = "."
                            nr_occupied -= 1

    world = {}
    for i in range(-7, 8):
        world_plane = [[elt for elt in line] for line in new[i]]
        world[i] = world_plane
    print(nr_occupied)

print(nr_occupied)

#part two
dirs2 = []
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            for WW in range(-1, 2):
                if [x, y, z, WW] != [0, 0, 0, 0]:
                    dirs2.append([x, y, z, WW])

nr_occupied2 = 29 # 29
for cycle in range(1, 7):
    new = {}


    for WW in range(-7, 8):
        for z in range(-7, 8):
            new[(WW, z)] = [[elt for elt in line] for line in galaxy[(WW, z)]]

    for WW in range(-cycle, cycle+1):
        for z in range(-cycle, cycle+1):
            for y, line in enumerate(galaxy[(WW, z)]):
                if y in [0, h-1]:
                    pass
                else:
                    for x, organism in enumerate(line):
                        if x in [0, w-1]:
                            pass
                        else:
                            neighbors = 0
                            for path in dirs2:
                                # print(path)
                                if galaxy[(WW+path[3],z+path[2])][y+path[1]][x+path[0]] == "#":
                                    neighbors += 1
                            
                            if neighbors == 3 and galaxy[(WW, z)][y][x] == ".":
                                new[(WW, z)][y][x] = "#"
                                nr_occupied2 += 1
                            if neighbors != 2 and neighbors != 3 and galaxy[(WW, z)][y][x] == "#":
                                new[(WW, z)][y][x] = "."
                                nr_occupied2 -= 1





    galaxy = {}
    for WW in range(-7, 8):
        for z in range(-7, 8):

            galaxy[(WW, z)] = [[elt for elt in line] for line in new[(WW, z)]]

    print(nr_occupied2)



print(nr_occupied2)