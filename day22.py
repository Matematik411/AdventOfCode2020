def play(one, two, dejavu):
    while one and two:
        #konec igre, ce ponovitev postavitve
        if (tuple(one), tuple(two)) in dejavu:
            return (1, one, two)
        else:
            dejavu.add((tuple(one), tuple(two)))
        a = one[0]
        del one[0]
        b = two[0]
        del two[0]

        #moramo v pod-igro
        if len(one) >= a and len(two) >= b:
            lower_game = play(one[:a], two[:b], set())[0]
            if lower_game == 1:
                one.append(a)
                one.append(b)
            else:
                two.append(b)
                two.append(a)


        else: #igra se navadno
            if a > b:
                one.append(a)
                one.append(b)
            
            else:
                two.append(b)
                two.append(a)
    if one:
        return (1, one, two)
    else:
        return (2, one, two)

#podatki
fst = []
snd = []
input()
for i in range(2):
    for _ in range(25):
        a = int(input())
        if i == 0:
            fst.append(a)
        else:
            snd.append(a)

    if i == 0:
        input()
        input()

#for part two
parttwo_fst = fst.copy()
parttwo_snd = snd.copy()

#part one
while (fst) and (snd):
    a = fst[0]
    del fst[0]
    b = snd[0]
    del snd[0]

    if a > b:
        fst.append(a)
        fst.append(b)
    
    else:
        snd.append(b)
        snd.append(a)

if snd:
    print("Winner of the first round is the second player!")
    result = 0
    l = len(snd)
    for x in range(l):
        result += (l-x) * snd[x]
else:
    print("Winner of the first round is the first player!")
    result = 0
    l = len(fst)
    for x in range(l):
        result += (l-x) * fst[x]
print(result)



#part two
winner, end_fst, end_snd = play(parttwo_fst, parttwo_snd, set())
if winner == 1:
    print("Winner of the second round is the first player!")
    result = 0
    l = len(end_fst)
    for x in range(l):
        result += (l-x) * end_fst[x]
else:
    print("Winner of the second round is the second player!")
    result = 0
    l = len(end_snd)
    for x in range(l):
        result += (l-x) * end_snd[x]
print(result)