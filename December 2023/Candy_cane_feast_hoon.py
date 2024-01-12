#Did not work because O(n^3) (I was unaware at the time)

l1 = input().split()
l2 = input().split()
l3 = input().split()

cows = []
canes = []

for i in range(int(l1[0])):
    cows.append(int(l2[i]))

for j in range(int(l1[1])):
    canes.append(int(l3[j]))

for cane in range(len(canes)):
    cane = list(range(canes[cane]+1))
    cane.pop(0)
    for cow in range(len(cows)):
        grow = 0
        for i in range(len(cane)):
            if cows[cow] >= cane[0]:
                grow += 1
                cane.pop(0)
            elif cows[cow] not in cane:
                break
        cows[cow] += grow


for i in range(len(cows)):
    print(cows[i])

