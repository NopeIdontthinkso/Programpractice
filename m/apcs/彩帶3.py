m, n = map(int, input().split())
list1 = [int(x) for x in input().split()]
ans = 0
list2 = []
for i in range(m):
    list2.append(list1[i])
for i in range(len(list1)-m+1):
    a = 0
    for j in range(m):
        for s in range(m-j):
            if j != s+j:
                if list2[j] == list2[s+j]:
                    a += 1
    if a == 0:
        ans += 1
    list2.pop(0)
    if i+m < len(list1):
        list2.append(list1[i+m])

print(ans)
                 