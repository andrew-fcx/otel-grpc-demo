import grpc
import random_pb2
import random_pb2_grpc
import time


def get_random_number(stub, minimum, maximum):
    min_max = random_pb2.MinMax(minimum=minimum, maximum=maximum)
    res = stub.getNum(min_max)
    n = res.num
    
    print("Random number was:", n)
    
    return n


def run(min=1, max=100, sleep_time=1):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = random_pb2_grpc.RandNumGenStub(channel)

        while True:
            r = get_random_number(stub, min, max)
            time.sleep(sleep_time)


if __name__ == "__main__":
    run()
