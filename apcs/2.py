l1 = [int(x) for x in input().split()]
l2 = []
l3 = []
l4 = []
for i in range(l1[0]):
    l2.append([int(x) for x in input().split()])
for i in range(len(l2)):
    l3.append(max(l2[i]))
print(sum(l3))
for i in range(len(l3)):
    if sum(l3)%l3[i] == 0:
        l4.append(l3[i])
if l4:
    print(*l4)
else:
    print(-1)
