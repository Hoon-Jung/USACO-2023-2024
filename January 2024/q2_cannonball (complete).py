lennumline, spot = map(int, input().split())
numline = []
spot -= 1
numtargets = 0

for i in range(lennumline):
    numline.append(list(map(int, input().split())))
    if numline[-1][0] == 1:
        numtargets += 1

power = 1
targets = 0
its = 0
numlinelen = lennumline * 10

while True:
    if numline[spot][0] == 0:
        if power > 0:
            power += numline[spot][1]
            power = power * -1
        else:
            power -= numline[spot][1]
            power = power * -1
    elif numline[spot][0] == 1 and abs(power) >= numline[spot][1]:
        numline[spot][0] += 1
        targets += 1
    spot += power
    its += 1
    if spot < 0 or spot >= lennumline or numtargets == targets or its >= numlinelen:
        break

print(targets)