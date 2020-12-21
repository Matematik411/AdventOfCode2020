known = {} # slovar food: alergen
data = []
apperances = {}
while True:
    try:
        a = input().split("(")
        food = set(a[0].split())
        alergens = set(a[1][9:-1].split(", "))
        for case in alergens:
            if case not in apperances:
                apperances[case] = 1
            else:
                apperances[case] += 1
        data.append([food, alergens])
    except:
        break
apperances = [[k, v] for k, v in apperances.items()]
list(apperances).sort(key = lambda x:x[1])

i = 0
while apperances:
    most_common = apperances[i][0]
    in_all = set()
    for case in data:
        if most_common in case[1]:
            if in_all == set():
                in_all = case[0]
            else:
                in_all = in_all.intersection(case[0])
    if len(in_all) == 1:
        food = list(in_all)[0]
        known[food] = most_common

        for case in data:
            if most_common in case[0]:
                case[1].remove(most_common) 
            if food in case[0]:
                case[0].remove(food)
        del apperances[i]
        i = 0
    else:
        i += 1


fst_part = 0
for case in data:
    fst_part += len(case[0])


known = [[k, v] for k, v in known.items()]
known.sort(key= lambda x : x[1])

canonical_dangerous_ingredient_list = ""
for case in known:
    canonical_dangerous_ingredient_list += case[0] + ","

print(fst_part)
print(canonical_dangerous_ingredient_list[:-1])