from Hashtable import Hashtable
import socket
from _thread import *

from constants import *

# hashtable = Hashtable()
# nServer = 1

class TcpServer:

    def __init__(self, hashtable: Hashtable) -> None:
        self.hashtable = hashtable
    
    def switch(self, data):
        case = data[0]
        print(case)
        if case == 0:
            # nServer = 0
            return END_TCP_CONNECTION
        elif case == 1:
            return self.createhash(data[1:])
        elif case == 2:
            return self.readhash(data[1:])
        elif case == 3:
            return self.updatehash(data[1:])
        elif case == 4:
            return self.deletehash(data[1:])
        else:
            return 5

    def createhash(self, data):
        KeySize = int(data[0])
        key = data[1:KeySize+1].decode()
        value = data[KeySize+1:].decode()

        return self.hashtable.create(key, value)

    def readhash(self, data):
        KeySize = int(data[0])
        key = data[1:KeySize+1].decode()
        return self.hashtable.read(key)

    def updatehash(self, data):
        KeySize = int(data[0])
        key = data[1:KeySize+1].decode()
        value = data[KeySize+1:].decode()
        return self.hashtable.update(key, value)

    def deletehash(self, data):
        KeySize = int(data[0])
        key = data[1:KeySize+1].decode()
        value = data[KeySize+1:].decode()
        return self.hashtable.delete(key, value)

    def threaded_client(self, c):
        while True:
            print('Esperando mensagem')
            data = c.recv(1024)
            retorno = self.switch(data)

            if retorno == END_TCP_CONNECTION:
                break

            if(retorno == SUCCESS):
                message = bytes((SUCCESS).to_bytes(1,'big'))
                c.send(message)
            elif(retorno == ERROR):
                message = bytes((ERROR).to_bytes(1,'big'))
                c.send(message)
            elif(type(retorno) == str):
                message = bytes((SUCCESS).to_bytes(1,'big')) + retorno.encode() 
                c.send(message)


    def serve(self):
        s = socket.socket()
        host = socket.gethostname()
        port =  12345
        s.bind((host, port))

        s.listen(5)

        while True:
            print('Esperando conexão...')
            c, addr = s.accept()
            print('Conectado')
            start_new_thread(self.threaded_client, (c, ))


# server()