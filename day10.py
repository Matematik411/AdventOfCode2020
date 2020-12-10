jolts = [0]
while True:
    try:
        a = int(input())
        jolts.append(a)
    except:
        break
jolts.sort()
jolts.append(jolts[-1] + 3)

diffs = [0, 0]
for i in range(1,len(jolts)):
    if jolts[i] - jolts[i-1] == 1:
        diffs[0] += 1
    elif jolts[i] - jolts[i-1] == 3:
        diffs[1] += 1

print(diffs[0]*diffs[1])

#part 2
paths = [0 for _ in range(len(jolts))]
paths[-1] = 1


for i in range(len(jolts)-2, -1,-1):
    from_here = 0

    for j in range(1, 4):
        try:
            if jolts[i+j] - jolts[i] < 4:
                from_here += paths[i+j]
        except:
            pass
    paths[i] = from_here

print(paths[0])
