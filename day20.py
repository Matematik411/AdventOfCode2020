nr_neighbors = {}
borders = {}
images = {}

# shrani skupne robove
def check(case, number, edge):
    if case in borders:
        nr_neighbors[borders[case][0][0]] += 1
        nr_neighbors[number] += 1
        borders[case].append((number, edge, 0))

    else:
        borders[case] = [(number, edge, 0)]

    case = case[::-1]
    if case in borders:
        nr_neighbors[borders[case][0][0]] += 1
        nr_neighbors[number] += 1
        borders[case].append((number, edge, 1))

    else:
        borders[case] = [(number, edge, 1)]


    return False

#prebere podatke
for _ in range(144):
    _, nr = input()[:-1].split()
    data = []
    nr = int(nr)
    nr_neighbors[nr] = 0
    for _ in range(10):
        data.append(input())
    input()
    
    flip = []
    border = data[0]
    flip.append(check(border, nr, 0))

    border = data[-1][::-1]
    flip.append(check(border, nr, 2))

    border = ""
    for i in range(9, -1, -1):
        border += data[i][0]
    flip.append(check(border, nr, 3))

    border = ""
    for i in range(10):
        border += data[i][-1]
    flip.append(check(border, nr, 1))
    
    images[nr] = data

#ker sem spreminjal kodo
resitev_ena = 29125888761511

#funkciji za obracanje/rotiranje kvadrata
def rotate(piece, where, n):
    nova = []
    if where == 1: #pozitivna smer
        for i in range(n):
            vrsta = ""
            for j in range(n):
                vrsta += piece[j][n-1-i]
            nova.append(vrsta)
    else:
        for i in range(n):
            vrsta = ""
            for j in range(n):
                vrsta += piece[n-1-j][i]
            nova.append(vrsta)
    return nova

def flip(piece, where, n):
    nova = []
    if where == 1: #navpicna os
        for i in range(n):
            nova.append(piece[i][::-1])
    else:
        for i in range(n):
            nova.append(piece[n-1-i])
    return nova

#zgradim mrezo, zacnem levo zgoraj z enim kotnim, ki ga poznam iz prvega dela. Obrnem ga, da res pase levo zgoraj
zacetni = images[2833]
zacetni = rotate(flip(zacetni, 1, 10), 1, 10)
index = 2833

#zgradim celo mrezo
mreza = [[0 for _ in range(12)] for _ in range(12)]
stevilke = [[0 for _ in range(12)] for _ in range(12)]
mreza[0][0] = zacetni
stevilke[0][0] = index


for i in range(12):
    for j in range(12):
        if j == 0: #gledamo gor, (0, 0) ze imamo
            if i > 0:
                index = stevilke[i-1][j] #prejsni
                trenutni = mreza[i-1][j]

                #rob po katerem gledam
                rob = ""
                for x in range(10):
                    rob = trenutni[9]
                sosedi = borders[rob]

                #poiscem naslednjega
                if sosedi[0][0] == index:
                    index = sosedi[1]
                else:
                    index = sosedi[0]

                #ga prav obrnem
                trenutni = images[index[0]]
                for _ in range(index[1]):
                    trenutni = rotate(trenutni, 1, 10)
                if index[2]:
                    trenutni = flip(trenutni, 1, 10)

                #in shranim
                index = index[0]
                mreza[i][j] = trenutni
                stevilke[i][j] = index

        #zgradimo celo vrstico, 
        else:
            trenutni = mreza[i][j-1]#prejsni

            #rob po katerem gledam
            rob = ""
            for x in range(10):
                rob += trenutni[x][9]
            sosedi = borders[rob]

            #poiscem naslednjega
            if sosedi[0][0] == index:
                index = sosedi[1]
            else:
                index = sosedi[0]

            #ga prav obrnem
            trenutni = images[index[0]]
            for _ in range(3-index[1]):
                trenutni = rotate(trenutni, 0, 10)
            if index[2] == 0:
                trenutni = flip(trenutni, 0, 10)

            #in shranim
            index = index[0]
            mreza[i][j] = trenutni
            stevilke[i][j] = index

# zdaj zgradim celo sliko (pobrisem skupne robove)
celota = []
for x in range(120):
    if x % 10 in [0, 9]:
        continue
    nov = ""
    for i in range(12):
        nov += mreza[x//10][i][x%10][1:-1]
    celota.append(nov)

    

#ugotovim, kako mora biti obrnjena slika, da so posasti vidne
celota = rotate(celota, 1, 96)
celota = rotate(celota, 1, 96)
celota = rotate(celota, 1, 96)

#ker bom spreminjal elemente spremenim v matriko
matricno = [[i for i in vrsta] for vrsta in celota]


#zdaj moram najti posasti, ki so naslednje oblike
loch_ness = [(1, 1), (3, 0), (1, -1), (1, 0), (1, 1), (3, 0), (1, -1), (1, 0), (1, 1), (3, 0), (1, -1), (1, -1), (0, 1), (1, 0)]

posasti = 0
x = 0 # x se vcasih ne premakne

while x < 96:
    for y in range(96):


        if matricno[y][x] == "#":
            cela = True
            a, b = x, y
            for premik in loch_ness:
                a, b = a+premik[0], b + premik[1]
                try:
                    if matricno[b][a] != "#":
                        cela = False
                        break
                except:
                    cela = False
                    break
            
            if cela:
                posasti += 1
                a, b = x, y
                matricno[b][a] = "O"
                for premik in loch_ness:
                    a, b = a+premik[0], b + premik[1]
                    matricno[b][a] = "O"
                break
    if not cela:
        x += 1

#vrnem nazaj v string obliko, da si lahko pogledam koncno sliko
celota = ["".join(vrsta) for vrsta in matricno]
print(celota)

#prestejem preostale #, to je resitev drugega dela
resitev_dva = 0
for x in matricno:
    resitev_dva += x.count("#")

print(resitev_ena)
print(resitev_dva)


    
