blacks = set()
positions = {}


while True:
    try:
        a = input()
        y_change = 0
        move = [0, 0]
        for x in a:
            if x == "n":
                y_change = 1
            elif x == "s":
                y_change = -1
            elif x == "e":
                if y_change == -1:
                    move[0] += 0
                    move[1] += -1
                else:
                    move[0] += 1
                    move[1] += y_change
                y_change = 0
            else:
                if y_change == 1:
                    move[0] += 0
                    move[1] += 1
                else:
                    move[0] += -1
                    move[1] += y_change
                y_change = 0


        move = tuple(move)

        if move in positions:
            positions[move] += 1
        else:
            positions[move] = 1
    except:
        break

for pos, val in positions.items():
    if val % 2 == 1:
        blacks.add(pos)
print(len(blacks))
part_one = len(blacks)

neighbors = [(1, 0), (0, -1), (-1, -1), (-1, 0), (0, 1), (1, 1)]

for day in range(100):
    positions = {}
    new = set()
    for pos in blacks:
        x, y = pos
        adjacent_black = 0
        for move in neighbors:
            a, b = move
            if (x+a, y+b) in blacks:
                adjacent_black += 1
            else:
                if (x+a, y+b) in positions:
                    positions[(x+a, y+b)] += 1
                else:
                    positions[(x+a, y+b)] = 1
        if adjacent_black in {1, 2}:
            new.add(pos)
    for pos, val in positions.items():
        if val == 2:
            new.add(pos)
    print(f"Day {day+1}: {len(new)}")
    blacks = new.copy()

print(f"Part one solution was {part_one}")


        
        

