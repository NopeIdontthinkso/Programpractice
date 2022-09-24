from sys import stdin
from collections import deque
lines = deque(stdin.readlines())

while lines:
    CODE = {'0 1 0 1': 'A',
            '0 1 1 1': 'B',
            '0 0 1 0': 'C',
            '1 1 0 1': 'D',
            '1 0 0 0': 'E',
            '1 1 0 0': 'F'}

    a = int(lines.popleft().strip())
    l1 = ''

    for i in range(a):
        b = lines.popleft().strip()
        l1 += CODE[b]

    print(l1)