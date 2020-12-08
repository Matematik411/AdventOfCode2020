orders = []
while True:
    try:
        a = input().split()
        orders.append([a[0], int(a[1])])
    except:
        break


def run_program():
    acc = 0
    visited = [0 for _ in range(len(orders))]
    i = 0
    finished = True
    while True:
        if i == len(orders):
            print("Finished well!")
            break
        if visited[i]:
            print("Infinite Loop!")
            finished = False
            break

        visited[i] = 1
        if orders[i][0] == "nop":
            i += 1
        elif orders[i][0] == "acc":
            acc += orders[i][1]
            i += 1
        else:
            i += orders[i][1]
    return visited, acc, finished

#prvi del
vis_fst, acc, flag = run_program()
print(acc)

#drugi del
for i, x in enumerate(vis_fst):
    if x == 1 and orders[i][0] == "jmp":
        orders[i][0] = "nop"
        _, acc, flag = run_program()
        if flag:
            print(acc)
            break
        else:
            orders[i][0] = "jmp"
    elif x == 1 and orders[i][0] == "nop":
        orders[i][0] = "jmp"
        _, acc, flag = run_program()
        if flag:
            print(acc)
            break
        else:
            orders[i][0] = "nop"


