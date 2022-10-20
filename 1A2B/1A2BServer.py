from random import randint
from os.path import dirname
import socket


HOST = '127.0.0.1'
PORT = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)


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
while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    anum = 0
    bnum = 0
    guesscode = clientMessage
    print('Client message is:', clientMessage)
    chance += -1
    for i in range(DIFFICULT):
        for j in range(DIFFICULT):
            if guesscode[i] == answer[j]:
                if i == j:
                    anum += 1
                else:
                    bnum += 1
    print(str(anum) + 'A' + str(bnum) + 'B')
    serverMessage = str(anum) + 'A' + str(bnum) + 'B'
    conn.sendall(serverMessage.encode())
    if anum == DIFFICULT:
        print('You Win')
        serverMessage = 'You Win'
        conn.sendall(serverMessage.encode())
        break
    if chance == 0:
        print('You Lose')
        serverMessage = 'You Lose'
        conn.sendall(serverMessage.encode())
        break
    conn.close()