import grpc
import os

from concurrent import futures
from hashtable_pb2 import *
from hashtable_pb2_grpc import *
from Hashtable import Hashtable
from constants import *
from dotenv import load_dotenv

class GrpcServer(HashtableServicer):

    def __init__(self, hashtable: Hashtable) -> None:
        super().__init__()
        
        self.hashtable = hashtable

    def create(self, request, context):
        key = request.key
        value = request.value
        print(f'key {key} value {value}')

        status = self.hashtable.create(key, value)

        return Response(status=status)
    
    def read(self, request, context):
        key = request.key
        readResponse = self.hashtable.read(key)
        
        print(readResponse)

        if type(readResponse) == str:
            return Response(status=SUCCESS, value=readResponse)

        return Response(status=ERROR, value='')

    def update(self, request, context):
        key = request.key
        value = request.value
        status = self.hashtable.update(key, value)

        return Response(status=status)

    def delete(self, request, context):
        key = request.key
        status = self.hashtable.delete(key)

        return Response(status=status)

    def serve(self):
        load_dotenv()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_HashtableServicer_to_server(self, server)
        port = int(os.getenv('GRPC_SERVER_PORT'))
        server.add_insecure_port(f'[::]:{port}')
        server.start()
        server.wait_for_termination()
