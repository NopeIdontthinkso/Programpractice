from random import randint
import socket

answer = ''
chance = 10
DIFFICULT = 4
ALLNUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(DIFFICULT):
    a = randint(0, 9-i)
    answer += ALLNUM[a]
    ALLNUM.remove(ALLNUM[a])

HOST = '127.0.0.1'
PORT = 8000
clientMessage = answer

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(clientMessage.encode())

serverMessage = str(client.recv(1024), encoding='utf-8')
print('Server:', serverMessage)

client.close()