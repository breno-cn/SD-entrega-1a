from hashtable_pb2_grpc import *
from hashtable_pb2 import *
import grpc
from dotenv import load_dotenv
import os

load_dotenv()
port = os.getenv('GRPC_SERVER_PORT')
address = f'localhost:{port}'

with grpc.insecure_channel(address) as channel:
    stub = HashtableStub(channel)

    while True:
        print('O que você deseja fazer?')
        option = int(input('1 -> CREATE\n2 -> READ\n3 -> UPDATE\n4 -> DELETE\n5 -> ENCERRAR\n'))

        if option == 1:
            key = input('Digite a chave: ')
            value = input('Digite o valor: ')

            status = stub.create(CreateRequest(key=key, value=value))
            print(str(status))


        if option == 2:
            key = input('Digite a chave: ')
            
            resp = stub.read(ReadRequest(key=key))
            print(str(resp))


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

