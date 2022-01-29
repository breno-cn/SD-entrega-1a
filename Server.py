from TcpServer import TcpServer
from GrpcServer import GrpcServer

from Hashtable import Hashtable
from _thread import *

hashtable = Hashtable()

tcpServer = TcpServer(hashtable)
grpcServer = GrpcServer(hashtable)

print('Inicializando servidor TCP...')
start_new_thread(lambda: tcpServer.serve(), ())

print('Inicializando servidor GRPC...')
start_new_thread(lambda: grpcServer.serve(), ())

while True:
    try:
        pass
    except KeyboardInterrupt:
        print('Encerrando servidor...')
        break
