sum_of_lines = 0
sum_of_lines2 = 0

def calculate(expr):
    result = 0
    if expr.count("(") == 0:
        expr = expr.split()
        n = len(expr)
        i = 0
        while i < (n-2):
            expr[i] = int(expr[i])
            expr[i+2] = int(expr[i+2])
            if expr[i+1] == "+":
                expr[i+2] += expr[i]
            elif expr[i+1] == "*":
                expr[i+2] *= expr[i]
            i += 2
        return expr[n-1]

    while expr.count(")") > 0:
        expr = expr.split("(")
        for i, e in enumerate(expr):
            if e.count(")") > 0:
                loc = e.index(")")
                partial = calculate(e[:loc])
                if loc == len(e) - 1:
                    expr[i] = str(partial)
                else:
                    expr[i] = str(partial) + e[loc+1:]
                break
        new = expr[0]
        for j, a in enumerate(expr[1:]):
            if j + 1 == i:
                new += a
            else:
                new += "(" + a
        expr = new
    expr = expr.replace("(", "")
    return calculate(expr)

def calculate_add(expr):
    result = 0
    if expr.count("(") == 0:
        #1st calulate all +
        expr = expr.split()
        for i, a in enumerate(expr):
            if i % 2 == 0:
                expr[i] = int(a)
        new = []
        n = len(expr)
        i = 0

        while i < (n-2):
            if expr[i+1] == "+":
                expr[i+2] += expr[i]

            elif expr[i+1] == "*":

                new.append(expr[i])
                new.append("*")

            i += 2

        new.append(expr[n-1])
        #2nd calculate *
        n = len(new)
        i = 0
        while i < (n-2):
            new[i+2] *= new[i]
            i += 2
        return new[n-1]


    while expr.count(")") > 0:
        expr = expr.split("(")
        for i, e in enumerate(expr):
            if e.count(")") > 0:
                loc = e.index(")")
                partial = calculate_add(e[:loc])
                if loc == len(e) - 1:
                    expr[i] = str(partial)
                else:
                    expr[i] = str(partial) + e[loc+1:]
                break
        new = expr[0]
        for j, a in enumerate(expr[1:]):
            if j + 1 == i:
                new += a
            else:
                new += "(" + a
        expr = new
    expr = expr.replace("(", "")
    return calculate_add(expr)



# print(calculate_add("5 + (8 * 3 + 9 + 3 * 4 * 3)"))

while True:
    try:
        line = input()
        sum_of_lines += calculate(line)
        sum_of_lines2 += calculate_add(line)

    except:
        break



print(sum_of_lines)
print(sum_of_lines2)