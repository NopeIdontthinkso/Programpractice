m, n = map(int, input().split())
list1 = [int(x) for x in input().split()]
ans = 0
for i in range(len(list1)-m+1):
    list2 = []
    a = 0
    for j in range(m):
        list2.append(list1[i+j])
    for j in range(m):
        for s in range(m):
            if j != s:
                if list2[j] == list2[s]:
                    a += 1
    if a == 0:
        ans += 1
print(ans)