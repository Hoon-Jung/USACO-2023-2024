powerlevel = int(input())
grass = list(map(int, input().split()))
amount = 0
gap = 0
prev = 0

for i in range(powerlevel):
    if grass[i] != 0:
        power = 0 - grass[i]
        amount += abs(power)
        for j in range(powerlevel-1-i):
            grass[j+i+1] += power * (j+2)
    
print(amount)