count = 0
count2 = 0

while True:

    questions = set()
    # 2nd part
    everyone = set()
    fst = True
    try:
        person = input()

        while person != "":
            for x in person:
                questions.add(x)

            if fst:
                for x in person:
                    everyone.add(x)
            else:
                this = set()
                for x in person:
                    this.add(x)
                everyone = everyone.intersection(this)


            person = input()
            fst = False

        count += len(questions)
        count2 += len(everyone)

    except:
        break
    #print(questions)

count += len(questions)
count2 += len(everyone)

print(count)
print(count2)