l1 = [int(x) for x in input().split()]
l2 = []
for i in range(l1[0]):
    l2.append([int(x) for x in input().split()])
l3 = [int(x) for x in input().split()]
l3.reverse()
for i in range(len(l3)):
    if l3[i]:
        l4 = []
        l4.append(l2[-1])
        l4.append(l2[0])
        l2[0] = l4[0]
        l2[-1] = l2[-1]  
    else:
        l4 = []
        for j in range(len(l2[0])):
            l4.append([l2])