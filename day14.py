memory1 = {}
memory2 = {}

def binary_nr(x, l):
    final = [0] * l
    i = 0
    while x > 0:
        a = x % 2
        final[l-1-i] = a
        x //= 2
        i += 1
    return final

def mask_alg(nr, m):
    number = 0
    for i in range(35, -1, -1):
        if m[i] == "1":
            nr[i] = 1
        elif m[i] == "0":
            nr[i] = 0
        number += nr[i] * (2**(35-i))
    return number

def mask_join(m, a):
    new = ""
    for x in m:
        if x != "X":
            new += x
        else:
            new += str(a.pop())
    return new

def mask_alg2(nr, m):
    number = ""
    for i in range(35, -1, -1):
        if m[i] == "0":
            pass
        elif m[i] == "1":
            nr[i] = 1
        else:
            nr[i] = "X"
        number += str(nr[i])
    return number[::-1]

def to_nr(x):
    a = 0
    for i in range(len(x)-1, -1, -1):
        a += int(x[i]) * 2**(len(x)-1-i)
    return a

def all_cases(m):
    numbers = []
    c = m.count("X")
    for i in range(2**c):
        case = mask_join(m, binary_nr(i, c))
        numbers.append(to_nr(case))

    return numbers


while True:
    try:
        a = input()
        if a[:4] == "mask":
            mask = a[7:]


        else:
            pos = a.split("]")[0][4:]
            val = a.split(" = ")[1]
            pos, val = int(pos), int(val)
            #part one
            memory1[pos] = mask_alg(binary_nr(val, 36), mask)
            #part two
            mask2 = mask_alg2(binary_nr(pos, 36), mask)
            for case in all_cases(mask2):
                memory2[case] = val



    except:
        break

print(sum(memory1.values()))
print(sum(memory2.values()))