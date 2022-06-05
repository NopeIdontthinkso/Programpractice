list1 = [int(x) for x in input().split()]
a = []
b = []
first_print = 0
second_print = float('inf')
asum = 0
arow = list1[0]
acol = list1[1]
brow = list1[2]
bcol = list1[3]
r = list1[4]
for i in range(arow):
    e = [int(x) for x in input().split()]
    asum += sum(e)
    a.append(e)
for i in range(brow):
    e = [int(x) for x in input().split()]
    b.append(e)
for i in range(brow - arow + 1):
    for j in range(bcol - acol +1):
        e = 0
        f = 0
        for s in range(arow):
            for t in range(acol):
                if b[i+s][j+t] != a[s][t]:
                    e += 1
                f += b[i+s][j+t]

        if e <= r:
            first_print += 1
            if abs(f-asum) < second_print:
                second_print = abs(f-asum)


print(first_print)
if second_print==float('inf'):
    print(-1)
else:
    print(second_print)



