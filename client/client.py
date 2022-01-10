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

    resp = int.from_bytes(s.recv(1024), byteorder='big', signed=True)

    if resp == 4:
        print('Sucesso na operação!')
        return
    
    if resp == 5:
        print('Ocorreu algum erro na sua operação!')

while True:
    print('O que você deseja fazer?')
    option = int(input('1 -> CREATE\n2 -> READ\n3 -> UPDATE\n4 -> DELETE\n5 -> ENCERRAR\n'))

    if option == 1:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = bytes(option) + keyLength.to_bytes(2, 'big') + key.encode() + value.encode()
        print(message)

        s.send(message)
        getResponse(s)

    if option == 2:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = bytes(option) + keyLength.to_bytes(2, 'big') + key.encode()
        print(message)

        s.send(message)
        getResponse(s)

    if option == 3:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = bytes(option) + keyLength.to_bytes(2, 'big') + key.encode() + value.encode()
        print(message)

        s.send(message)
        getResponse()

    if option == 4:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = bytes(option) + keyLength.to_bytes(2, 'big') + key.encode()
        print(message)

        s.send(message)
        getResponse(s)

    if option == 5:
        message = (0).to_bytes(2, 'big')
        s.send(message)
        s.close()
        break
