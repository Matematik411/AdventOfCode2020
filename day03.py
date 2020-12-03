gozd = []
while True:
    try:
        vrsta = input()
        gozd.append(vrsta)
    except:
        break
sirina = len(gozd[0])

zadane = 0
x = 0
zadane2 = 0
x2 = 0
zadane3 = 0
x3 = 0
zadane4 = 0 
x4 = 0
zadane5 = 0
x5 = [0, False]

for vrsta in gozd[1:]:
    x += 3
    x %= sirina
    if vrsta[x] == "#":
        zadane += 1
    
    x2 += 1
    x2 %= sirina
    if vrsta[x2] == "#":
        zadane2 += 1

    x3 += 5
    x3 %= sirina
    if vrsta[x3] == "#":
        zadane3 += 1    

    x4 += 7
    x4 %= sirina
    if vrsta[x4] == "#":
        zadane4 += 1
    
    if x5[1]:
        x5[0] += 1
        x5[0] %= sirina
        if vrsta[x5[0]] == "#":
            zadane5 += 1
        x5[1] = False
    else:
        x5[1] = True

print(zadane)
print(zadane*zadane2*zadane3*zadane4*zadane5)

