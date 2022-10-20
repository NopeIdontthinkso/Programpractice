import copy
m, n = map(int, input().split())
list1 = [int(x) for x in input().split()]
ans = 0
for i in range(len(list1)-m+1):
    list2 = []
    a = 0
    for j in range(m):
        list2.append(list1[j])
    b = len(list2)
    for j in range(m):
        list3 = copy.deepcopy(list2)
        for s in range(len(list3)-1,-1,-1):
            if list2[j] == list3[s]:
                list3.remove(list2[j])
        if len(list3) != (b-1):
            a+=1
    if a == 0:
        ans += 1
    list1.pop(0)
print(ans)