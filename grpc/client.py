import hashtable_pb2_grpc
import hashtable_pb2
import grpc

    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
with grpc.insecure_channel('localhost:50051') as channel:
    stub = hashtable_pb2_grpc.HashtableStub(channel)
    response = stub.read(hashtable_pb2.ReadRequest(key='nome'))
    print("Greeter client received: " + str(response))
