time = int(input())
buses = input().split(",")

#part one
min_delay = time
result = 0
for bus in buses:
    if bus != "x":
        delay = ((time // int(bus)) + 1)*int(bus) - time
        if delay <= min_delay:
            min_delay = delay
            result = delay * int(bus)

print(result)

#part two, preko teorije stevil, v iskanem trenutku ima prvi ostanek 0 po svojem modulu, ostali pa - svoj zamik, torej bus[1]-bus[0]
actuals = []
M = 1
for i, bus in enumerate(buses):
    if bus != "x":
        actuals.append([i, int(bus)])
        M *= int(bus)

for bus in actuals[1:]:
    bus[0] = bus[1]-bus[0]


def mod_inverse(a, m):
    k = 1
    x = a % m
    while x != 1:
        x = (x + a) % m
        k += 1
    return k

result = 0
for bus in actuals:
    if bus[0] != 0:
        b = M // bus[1]
        b2 = mod_inverse(b, bus[1])
        result += bus[0] * b * b2

result %= M
print(result)

