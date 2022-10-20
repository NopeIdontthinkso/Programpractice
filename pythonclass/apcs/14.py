n, m ,k = map(int, input().split())
alist = []
blist = []
live = []
ans = 0
for i in range(k):
    zlist = [int(x) for x in input().split()]
    alist.append(zlist)
for i in range(n):
    clist = []
    for j in range(m):
        clist.append(0)
    blist.append(clist)
for i in range(len(alist)):
    live.append(0)
while True:
    xlist = []
    z = 0
    for i in range(len(alist)):
        if live[i] == 0:
            blist[alist[i][0]][alist[i][1]] = 1
            alist[i][0] += alist[i][2]
            alist[i][1] += alist[i][3]
    for i in range(len(alist)):
        if alist[i][0] > m or alist[i][1] > n or alist[i][0]<0 or alist[i][1]<0:
            live[i] = 1
        elif blist[alist[i][0]][alist[i][1]] == 1 and alist[i][0] <= m and alist[i][1] <= n and live[i]==0 and alist[i][0]>=0 and alist[i][1]>=0:
            live[i] = 1
            xlist.append([alist[i][0], alist[i][1]])
    for i in range(len(xlist)):
        blist[xlist[i][0]][xlist[i][1]] = 0
    for i in range(len(live)):
        if live[i] == 1:
            z += 1
    if z == len(live):
        break
for i in range(m):
    for j in range(n):
        if blist[j][i] != 0:
            ans += 1
print(ans)