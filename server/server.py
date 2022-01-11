from Hashtable import Hashtable
import socket

hashtable = Hashtable()
nServer = 1

def switch(data):
    global nServer
    case = data[0]
    print(case)
    if case == 0:
        nServer = 0
        print('a')
        return 4
    elif case == 1:
        print('b')
        return createhash(data[1:])
    elif case == 2:
        print('c')
        return readhash(data[1:])
    elif case == 3:
        print('d')
        return updatehash(data[1:])
    elif case == 4:
        print('d')
        return deletehash(data[1:])
    else:
        print('e')
        return 5

def createhash(data):
    KeySize = int(data[0])
    key = data[1:KeySize+1]
    value = data[KeySize+1:]
    return hashtable.create(key, value)

def readhash(data):
    KeySize = int(data[0])
    key = data[1:KeySize+1]
    return hashtable.read(key)

def updatehash(data):
    KeySize = int(data[0])
    key = data[1:KeySize+1]
    value = data[KeySize+1:]
    return hashtable.update(key, value)

def deletehash(data):
    KeySize = int(data[0])
    key = data[1:KeySize+1]
    value = data[KeySize+1:]
    return hashtable.delete(key, value)

def server():
    s = socket.socket()
    host = socket.gethostname()
    port =  12345
    s.bind((host, port))

    s.listen(5)

    while nServer:
        print('Esperando conexão...')
        c, addr = s.accept()
        print('Conectado')
        while nServer:
            print('Esperando mensagem')
            data = c.recv(1024)
            print(f'data: {data}')
            retorno = switch(data)

            if(retorno == 4):
                message = bytes((4).to_bytes(1,'big'))
                c.send(message)
            elif(retorno == 5):
                message = bytes((5).to_bytes(1,'big'))
                c.send(message)
            elif(type(retorno) == str):
                message = bytes((4).to_bytes(1,'big')) + retorno.encode() 
                c.send(message)


server()