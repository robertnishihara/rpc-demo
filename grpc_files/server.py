import time
import messages_pb2

class Greeter(messages_pb2.BetaGreeterServicer):

  def SayHello(self, request, context):
    print "Received message from {}.".format(request.name)
    return messages_pb2.HelloReply(message="Hello {}.".format(request.name))

server = messages_pb2.beta_create_Greeter_server(Greeter())
server.add_insecure_port('[::]:50051')
server.start()
time.sleep(10000)
