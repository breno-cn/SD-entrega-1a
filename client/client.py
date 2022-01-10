import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

print('Conectando-se ao servidor...')
s.connect((host, port))

while True:
    print('O que você deseja fazer?')
    option = int(input('1 -> CREATE\n2 -> READ\n3 -> UPDATE\n4 -> DELETE\n5 -> ENCERRAR\n'))

    if option == 1:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = bytes(option) + bytes(keyLength) + key.encode() + value.encode()
        print(message)

    if option == 2:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = bytes(option) + bytes(keyLength) + key.encode()
        print(message)

    if option == 3:
        key = input('Digite a chave: ')
        value = input('Digite o valor: ')
        keyLength = len(key)

        message = bytes(option) + bytes(keyLength) + key.encode() + value.encode()
        print(message)

    if option == 4:
        key = input('Digite a chave: ')
        keyLength = len(key)

        message = bytes(option) + bytes(keyLength) + key.encode()
        print(message)

    if option == 5:
        break
