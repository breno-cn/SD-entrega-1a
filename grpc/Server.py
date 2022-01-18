from concurrent import futures
import grpc
import hashtable_pb2_grpc
import hashtable_pb2
from Hashtable import Hashtable


class Server(hashtable_pb2_grpc.HashtableServicer):

    hashtable = Hashtable()

    def create(self, request, context):
        key = request.key
        value = request.value
        print(f'key {key} value {value}')

        status = Server.hashtable.create(key, value)

        return hashtable_pb2.Response(status=status)
    
    def read(self, request, context):
        key = request.key
        readResponse = Server.hashtable.read(key)
        
        print(readResponse)

        if type(readResponse) == str:
            return hashtable_pb2.Response(status=4, value=readResponse)

        return hashtable_pb2.Response(status=5, value='')

    def update(self, request, context):
        key = request.key
        value = request.value
        status = Server.hashtable.update(key, value)

        return hashtable_pb2.Response(status=status)

    def delete(self, request, context):
        key = request.key
        status = Server.hashtable.delete(key)

        return hashtable_pb2.Response(status=status)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hashtable_pb2_grpc.add_HashtableServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()
