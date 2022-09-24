n = int(input())
alist = list(input())
astr = str()
t1 = str()
t2 = str()
ans = 0
for i in alist:
    if i.islower():
        astr += '0'
    else:
        astr += '1'
for i in range(n):
    t1 += '0'
    t2 += '1'
t3 = t1 + t2
t4 = t2 + t1
if t1 in astr or t2 in astr:
    ans = n
if (t4 in astr) or (t3 in astr):
    ans = n*2
    for i in range(1, len(astr)):
        if (t4*i in astr) or (t3*i in astr):
            ans = n*2*i
            if (t4*i+t2 in astr) or (t3*i+t1) in astr:
                ans = n*2*i + n
print(ans)