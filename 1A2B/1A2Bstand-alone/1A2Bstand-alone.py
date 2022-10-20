from random import randint
from os.path import dirname


answer = ''
chance = 10
DIFFICULT = 4
ALLNUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
file = open(dirname(__file__) + '/1.txt', 'w')
for i in range(DIFFICULT):
    a = randint(0, 9-i)
    answer += ALLNUM[a]
    ALLNUM.remove(ALLNUM[a])
file.write(answer)
file.close()
anum = 0
bnum = 0
for i in range(chance):
    anum = 0
    bnum = 0
    guesscode = str(input())
    chance += -1
    for i in range(DIFFICULT):
        for j in range(DIFFICULT):
            if guesscode[i] == answer[j]:
                if i == j:
                    anum += 1
                else:
                    bnum += 1
    print(str(anum) + 'A' + str(bnum) + 'B')
    if anum == DIFFICULT:
        print('You Win')
        break
    if chance == 0:
        print('You Lose')
        break