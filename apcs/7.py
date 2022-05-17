from collections import deque
l1 = [int(x) for x in input().split()]
l2 = deque([int(x) for x in input().split()])
a = l2[0]
l2.popleft()
b = 1
c = 0
d = l1[1]
for i in range(len(l2)):
    if b == 1:
        if l2[i] >= (a+d):
            c += l2[i] - a
            a = l2[i]
            b = 0
    else:
        if l2[i] <= (a-d):
            a = l2[i]
            b = 1
print(c)
