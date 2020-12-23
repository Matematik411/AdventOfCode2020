cups = [9,6,3,2,7,5,4,8,1]
# cups = [3,8,9,1,2,5,4,6,7]

current = 0

for _ in range(100):
    current_item = cups[current]

    chosen_items = [cups[(current+1)%9], cups[(current+2)%9], cups[(current+3)%9]]
    chosen = [(current+1)%9, (current+2)%9, (current+3)%9]
    for i in sorted(chosen,reverse=True):
        del cups[i]


    destination_item = current_item - 1
    if destination_item == 0:
        destination_item += 9
    while destination_item in chosen_items:
        destination_item = destination_item - 1
        if destination_item == 0:
            destination_item += 9

    destination = cups.index(destination_item)

    cups = cups[:destination+1] + chosen_items + cups[destination+1:]

    current = (cups.index(current_item)+1) % 9


result_one = ""
start = cups.index(1)
for i in range(1, 9):
    result_one += str(cups[(start+i) % 9])

print(result_one)

# part two - takes ~40s
N = 1000000
cups = [9,6,3,2,7,5,4,8,1] + [i for i in range(10, N+1)]
next_elt = {}
for i in range(N):
    if i == N-1:
        next_elt[cups[i]] = cups[0]
    else:
        next_elt[cups[i]] = cups[i+1]


current_item = cups[0]
for aaa in range(N*10):
    next_item = next_elt[current_item]

    chosen_items = []
    for _ in range(3):
        chosen_items.append(next_item)
        next_item = next_elt[next_item]
    next_elt[current_item] = next_item



    destination_item = current_item - 1
    if destination_item == 0:
        destination_item += N
    while destination_item in chosen_items:
        destination_item = destination_item - 1
        if destination_item == 0:
            destination_item += N

    end = next_elt[destination_item]

    next_elt[destination_item] = chosen_items[0]
    next_elt[chosen_items[2]] = end

    current_item = next_elt[current_item]
    # print(aaa)


result_two = next_elt[1] * next_elt[next_elt[1]]

print(result_two)