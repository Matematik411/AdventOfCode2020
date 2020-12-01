list = [int(input()) for _ in range(200)]
list.sort()

stop = False

i = 0
j = 199
while i < 199:
    if stop:
        break
    while j-i>0:
        if list[i] + list[j] == 2020:
            print(list[i]*list[j])
            stop = True
            break
        elif list[i] + list[j] < 2020:
            break
        j -=1
    i +=1
    j = 199


i = 0
j = 0
k = 199

stop = False

while i < 198:
    if stop:
        break
    while j < 199:
        if stop:
            break
        while k > j:
            if list[i] + list[j] + list[k] == 2020:
                print(list[i]*list[j]*list[k])
                stop = True
                break
            elif list[i] + list[j] + list[k] < 2020:
                break
            k -=1
        j +=1
        k = 199
    i +=1
    j = i
    k = 199