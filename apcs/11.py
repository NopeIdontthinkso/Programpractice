n = int(input())
m = int(input())
alist = []
anslist = []
for i in range(n):
    blist = [int(x) for x in input().split()]
    alist.append(blist)
if m == 0:
    for i in range(n):
        for j in range(n):
            anslist.append(alist[(n+1)/2][(n+1)/2])