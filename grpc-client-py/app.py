import grpc
import random_pb2
import random_pb2_grpc
import time
import argparse

from opentelemetry import trace
from opentelemetry import metrics

from logger import logger


tracer = trace.get_tracer(__name__)
meter = metrics.get_meter(__name__)


random_counter = meter.create_counter(
    "received_random_numbers_count",
    description="Number of random values received",
)


def get_random_number(stub, minimum, maximum):
    with tracer.start_as_current_span("get_random_number") as rng_span:
        rng_span.set_attribute("rng.minimum", minimum)
        rng_span.set_attribute("rng.maximum", maximum)
        
        min_max = random_pb2.MinMax(minimum=minimum, maximum=maximum)
        res = stub.getNum(min_max)
        n = res.num
        
        logger.info(f"Random number was: {n}")
    
    return n


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', type=int)
    parser.add_argument('--max', type=int)
    parser.add_argument('--sleep', type=int)
    
    return parser


def run(min=1, max=100, sleep_time=1):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = random_pb2_grpc.RandNumGenStub(channel)

        while True:
            r = get_random_number(stub, min, max)
            random_counter.add(1)
            time.sleep(sleep_time)


if __name__ == "__main__":
    args = init_parser().parse_args()
    
    mini = args.min if args.min else 1
    maxi = args.max if args.max else 100
    sleep_dir = args.sleep if args.sleep else 1
    
    run(min=mini, max=maxi, sleep_time=sleep_dir)
