from concurrent import futures
import grpc
import hashtable_pb2_grpc
import hashtable_pb2

class Server(hashtable_pb2_grpc.HashtableServicer):
    
    def read(self, request, context):
        return hashtable_pb2.Response(status=1, value='aaaaaaaaa')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hashtable_pb2_grpc.add_HashtableServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

serve()
