prevs = [int(input()) for _ in range(25)]
stack = [prevs[i] for i in range(25)]
stack_sum = sum(stack)
target = 26796446
found = False
start_stack = 0

def is_sum(a):
    for i, x in enumerate(prevs):
        for y in prevs[i+1:]:
            if x + y == a:
                return True


i = 0
while True:
    try:
        a = int(input())

        #drugi del
        if not found:
            stack.append(a)
            stack_sum += a
            #ce smo cez, se premaknemo naprej
            while stack_sum > target:
                stack_sum -= stack[start_stack]
                start_stack += 1

            if stack_sum == target:
                found = True
                print(max(stack[start_stack:]) + min(stack[start_stack:]))

        #prvi del
        if is_sum(a):
            prevs[i] = a
            i += 1
            i %= 25
        else:
            print(a)
            break
    except:
        break