import messages_pb2
from grpc.beta import implementations

channel = implementations.insecure_channel('localhost', 50051)
stub = messages_pb2.beta_create_Greeter_stub(channel)

import IPython
IPython.embed()
