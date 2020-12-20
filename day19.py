from functools import lru_cache
cond_dict = {30: "a", 20:"b"}

# tu dela le del 1, letosnji JOKER porabljen, ker nisem znal drugega dela


while True:
    line = input().split("|")

    if line == [""]:
        break
    if line[0][:3] in {"30:", "20:"}:

        continue
    nr, fst = line[0].split(":")
    data = [tuple(map(int, fst.strip().split()))]
    for additional in line[1:]:
        data.append(tuple(map(int, additional.strip().split())))
    cond_dict[int(nr)] = data
    
cond_dict2 = cond_dict.copy()
cond_dict2[8] = [(42,)*i for i in range(1, 3)]
cond_dict2[11] = [tuple([42]*i + [31]*i) for i in range(1, 3)]


# @lru_cache(maxsize=None)
# def generate(cond):
#     # print(cond)
#     if cond in {20, 30}:
#         return {cond_dict[cond]}
    
#     else:
#         together = set()
#         for case in cond_dict[cond]:
#             if len(case) == 1:
#                 for x in generate(case[0]):
#                     together.add(x)
#             else:
#                 fst = generate(case[0])
#                 snd = generate(case[1])
#                 for x in fst:
#                     for y in snd:
#                         together.add(x + y)
#         return together

@lru_cache(maxsize=None)
def generate(cond):
    if cond in {20, 30}:
        return {cond_dict[cond]}
    
    else:
        together = set()
        for case in cond_dict[cond]:
            options = [generate(i) for i in case]
            for i in range(1,len(options)):
                new = set()
                for x in options[i-1]:
                    for y in options[i]:
                        new.add(x + y)
                options[i] = new
            for one in options[-1]:
                together.add(one)
             
        return together

@lru_cache(maxsize=None)
def generate2(cond):
    if cond in {20, 30}:
        return {cond_dict2[cond]}
    
    else:
        together = set()
        for case in cond_dict2[cond]:
            options = [generate2(i) for i in case]
            for i in range(1,len(options)):
                new = set()
                for x in options[i-1]:
                    for y in options[i]:
                        new.add(x + y)
                options[i] = new
            for one in options[-1]:
                together.add(one)
             
        return together

posibilities = generate(0)
print("here")
# posibilities2 = generate2(0)
# print("there")

# a = generate(31)
# a2 = generate2(31)
# a3 = a.intersection(a2)
# print(a)
# print(a2, len(a2))
# print(a3, len(a3))
# print(cond_dict[8])
# print(cond_dict2[8])

matches = 0
matches2 = 0
# longest = 0
while True:
    try:
        a = input()
        # longest = max(longest, len(a))
        if a in posibilities:
            matches += 1
        # if a in posibilities2:
        #     matches2 += 1
    except:
        break

print(matches)
print(matches2)
# print(longest, longest_pattern)
# part two-------------
#42 in 31 generirata dolzine 

