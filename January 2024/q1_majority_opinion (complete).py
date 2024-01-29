def findmajorities(favorites, favlen):
    majorities = []
    if favlen < 4:
        favs = set()
        for i in range(favlen):
            if favorites.count(favorites[i]) > favlen // 2 and favorites[i] not in favs:
                majorities.append(int(favorites[i]))
                favs.add(favorites[i])
            else:
                favs.add(favorites[i])
        if majorities == []:
            return ["-1"]
        else:
            return majorities
    
    temp = [favorites[0], favorites[1], favorites[2]]
    favs = set()
    for i in range(favlen - 3):
        for j in range(2):
            if temp.count(temp[j]) > 1 and temp[j] not in favs:
                majorities.append(int(temp[j]))
                favs.add(temp[j])
        temp.pop(0)
        temp.append(favorites[i+3])
    for n in range(2):
        if temp.count(temp[n]) > 1 and temp[n] not in favs:
            majorities.append(int(temp[n]))
            favs.add(temp[n])
    if majorities == []:
        return ["-1"]
    else:
        return majorities


t = int(input())
for i in range(t):
    n = int(input())
    cows = input().split()
    ans = findmajorities(cows, n)
    ans.sort()
    printans = ""
    for m in range(len(ans)):
        if m == len(ans) - 1:
            printans += str(ans[m])
        else:
            printans += str(ans[m]) + " "
    print(printans)