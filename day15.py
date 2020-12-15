numbers = [2, 0, 1, 9, 5, 19]

spoken = {}
for i in range(len(numbers)):
    spoken[numbers[i]] = i+1
last = numbers[-1]
a = 0

for time in range(len(numbers) + 1, 30000000):# part one 2020
    if a not in spoken:
        spoken[a] = time
        a = 0
    else:
        spoken[a], a = time, time-spoken[a]


print(a)