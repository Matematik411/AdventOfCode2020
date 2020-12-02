import re

pravilni_1 = 0
pravilni_2 = 0

while True:
    try:
        s = input()
    except:
        break
    if s=="":
        break
    s = s.split(":")
    _, m, M, x, _ = re.compile("(\d+)-(\d+)\s(.)").split(s[0])
    #prvi del
    if int(m) <= s[1].count(x) <= int(M):
        pravilni_1 +=1
    #drugi del
    pojavitve = 0
    s = s[1][1:]
    if s[int(m)-1] == x:
        pojavitve += 1
    if s[int(M)-1] == x:
        pojavitve += 1
    if pojavitve == 1:
        pravilni_2 += 1




print(pravilni_1)
print(pravilni_2)