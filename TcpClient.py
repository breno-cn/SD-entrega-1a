import socket
from constants import SUCCESS, ERROR
from dotenv import load_dotenv
import os

load_dotenv()
s = socket.socket()
host = socket.gethostname()
port = int(os.getenv('TCP_SERVER_PORT'))

print('Conectando-se ao servidor...')
s.connect((host, port))

def getResponse(s):
    resp = s.recv(1024)
    status = resp[0]

    if status == SUCCESS:
        return status, resp
    
    if status == ERROR:
        return status, ''

while True:
    print('O que voce deseja fazer?')
    option = int(input('1 -> CREATE\n2 -> READ\n3 -> UPDATE\n4 -> DELETE\n5 -> ENCERRAR\n'))

    if option == 1:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode() + value.encode()

        s.send(message)
        status, resp = getResponse(s)
        print(status)

    if option == 2:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode()

        s.send(message)
        status, resp = getResponse(s)
        if status == SUCCESS:
            print(f'resposta READ: {resp[1:]}')
        else:
            print(f'status: {status}')

    if option == 3:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode() + value.encode()

        s.send(message)
        status, resp = getResponse(s)
        print(status)

    if option == 4:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode()

        s.send(message)
        status, resp = getResponse(s)
        print(status)

    if option == 5:
        message = (0).to_bytes(1, 'big')
        s.send(message)
        s.close()
        break
