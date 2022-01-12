from hashtable_pb2_grpc import *
from hashtable_pb2 import *
import grpc

    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = hashtable_pb2_grpc.HashtableStub(channel)
#     response = stub.read(hashtable_pb2.ReadRequest(key='nome'))
#     print("Greeter client received: " + str(response))

#     response = stub.update(hashtable_pb2.UpdateRequest(key='nome', value='David'))
#     print(str(response))

#     response = stub.delete(hashtable_pb2.DeleteRequest(key='nome'))
#     print(str(response))

#     response = stub.read(hashtable_pb2.ReadRequest(key='nome'))
#     print(str(response))

with grpc.insecure_channel('localhost:50051') as channel:
    stub = HashtableStub(channel)

    while True:
        print('O que você deseja fazer?')
        option = int(input('1 -> CREATE\n2 -> READ\n3 -> UPDATE\n4 -> DELETE\n5 -> ENCERRAR\n'))

        if option == 1:
            key = input('Digite a chave: ')
            value = input('Digite o valor: ')

            status = stub.read(CreateRequest(key=key, value=value))
            print(str(status))


        if option == 2:
            key = input('Digite a chave: ')
            
            resp = stub.read(ReadRequest(key=key))
            print(str(status))


        if option == 3:
            key = input('Digite a chave: ')
            value = input('Digite o valor: ')

            resp = stub.update(UpdateRequest(key=key, value=value))
            print(str(resp))


        if option == 4:
            key = input('Digite a chave: ')

            resp = stub.delete(DeleteRequest(key=key))
            print(str(resp))


        if option == 5:
            break

