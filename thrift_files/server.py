import sys
sys.path.append('gen-py')

from messages import Greeter

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class GreeterHandler:

  def SayHello(self, name):
    print "Received message from {}.".format(name)
    return "Hello {}.".format(name)

if __name__ == '__main__':
  handler = GreeterHandler()
  processor = Greeter.Processor(handler)
  transport = TSocket.TServerSocket(port=9090)
  tfactory = TTransport.TBufferedTransportFactory()
  pfactory = TBinaryProtocol.TBinaryProtocolFactory()

  server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
  server.serve()
