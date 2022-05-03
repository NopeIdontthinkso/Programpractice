l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l3 = [int(x) for x in input().split()]
l4 = [int(x) for x in input().split()]

a = 0

if sum(l1) > sum(l2):
    a += 1
else:
    a -= 1
if sum(l3) > sum(l4):
    a += 1
else:
    a -= 1

print(str(sum(l1))+ ':' + str(sum(l2)))
print(str(sum(l3))+ ':' + str(sum(l4)))

if a > 0:
    print('win')
elif a < 0:
    print('lose')
else:
    print('tie')