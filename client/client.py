import socket

SUCCESS = 4
ERROR = 5

s = socket.socket()
host = socket.gethostname()
port = 12345

print('Conectando-se ao servidor...')
s.connect((host, port))

def getResponse(s):
    print('Esperando resposta...')

    resp = s.recv(1024)
    status = resp[0]
    print(f'resposta: {resp}')

    if status == 4:
        print('Sucesso na operação!')
        return status, resp
    
    if status == 5:
        print('Ocorreu algum erro na sua operação!')
        return status, ''

while True:
    print('O que você deseja fazer?')
    option = int(input('1 -> CREATE\n2 -> READ\n3 -> UPDATE\n4 -> DELETE\n5 -> ENCERRAR\n'))

    if option == 1:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode() + value.encode()
        print(message)

        s.send(message)
        getResponse(s)

    if option == 2:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode()
        print(message)

        s.send(message)
        status, resp = getResponse(s)
        if status == 4:
            print(f'resposta READ: {resp[1:]}')

    if option == 3:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode() + value.encode()
        print(message)

        s.send(message)
        getResponse(s)

    if option == 4:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = option.to_bytes(1, 'big') + keyLength.to_bytes(1, 'big') + key.encode()
        print(message)

        s.send(message)
        getResponse(s)

    if option == 5:
        message = (0).to_bytes(1, 'big')
        s.send(message)
        s.close()
        break
