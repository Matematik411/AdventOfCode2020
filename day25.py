#input
card = 9033205
door = 9281649

subject = 7
base = 20201227
nr_door = 1
nr_card = 1

loop_door = 0
while nr_door != door:
    nr_door *= subject
    nr_door %= base
    loop_door += 1

subject = card
final = 1
for _ in range(loop_door):
    final *= subject
    final %= base

print(final)
#That's it folks!
