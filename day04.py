valids = 0

req = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}

while True:
    has = set()
    try:
        line = input().split()
        while line != []:
            for elt in line:
                k, v = elt.split(":")
                if k == "cid":
                    pass
                elif k == "byr" and (1920<=int(v)<=2002):
                    has.add(k)
                elif k == "iyr" and (2010<=int(v)<=2020):
                    has.add(k)
                elif k == "eyr" and (2020<=int(v)<=2030):
                    has.add(k)
                elif k == "hgt" and ((v[-2:]=="cm" and 150<=int(v[:-2])<=193) or (v[-2:]=="in" and (59<=int(v[:-2])<=76))):
                    has.add(k)
                elif k == "hcl" and (v[0]=="#"):
                    add = True
                    for x in v[1:]:
                        if x not in "0123456789abcdef":
                            add = False
                    if add:
                        has.add(k)
                elif k == "ecl" and (v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    has.add(k)
                elif k == "pid" and (len(v)==9):
                    add = True
                    for x in v:
                        if x not in "0123456789":
                            add = False
                    if add:
                        has.add(k)
            line = input().split()
    except:
        break
    if has == req:
        valids += 1

#zadnjega dodam ročno
for elt in line:
    k, v = elt.split(":")
    if k == "cid":
        pass
    elif k == "byr" and (1920<=int(v)<=2002):
        has.add(k)
    elif k == "iyr" and (2010<=int(v)<=2020):
        has.add(k)
    elif k == "eyr" and (2020<=int(v)<=2030):
        has.add(k)
    elif k == "hgt" and ((v[-2:]=="cm" and 150<=int(v[:-2])<=193) or (v[-2:]=="in" and (59<=int(v[:-2])<=76))):
        has.add(k)
    elif k == "hcl" and (v[0]=="#"):
        add = True
        for x in v[1:]:
            if x not in "0123456789abcdef":
                add = False
        if add:
            has.add(k)
    elif k == "ecl" and (v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        has.add(k)
    elif k == "pid" and (len(v)==9):
        add = True
        for x in v:
            if x not in "0123456789":
                add = False
        if add:
            has.add(k)
if has == req:
    valids += 1
print(valids)

