import re

condNr = []
while True:
    try :
        a = input()
        condNr.append(re.findall("([0-9]+\s)?([a-z]* [a-z]* bag)", a))
    except:
        break


#1st part
before = {}

for case in condNr:
    for color in case[1:]:
        if color[1] in before:
            before[color[1]].add(case[0][1])
        else:
            before[color[1]] = {case[0][1]}
    if case[0][1] not in before:
        before[case[0][1]] = set()

# dfs iz shiny gold bag
visited = set()
s = "shiny gold bag"
stack = [s]

while stack:
    now = stack.pop()
    if now in visited:
        continue
    visited.add(now)

    for parent in before[now]:
        if parent not in visited:
            stack.append(parent)

print(len(visited) - 1)


#2nd part
after = {}

for case in condNr:
    if case[0][1] not in after:
        after[case[0][1]] = set(case[1:])
    else:
        after[case[0][1]] = after[case[0]].union(set(case[1:]))

def count_bags(x):
    bags = 0
    for child in after[x]:
        try:
            bags += int(child[0])*(1 + count_bags(child[1]))
        except:
            continue
    return bags

count = 0
s = "shiny gold bag"

for child in after[s]:
    count += int(child[0])*(1 + count_bags(child[1]))


print(count)