# RPC Demo

This repository contains instructions for trying out [Apache Thrift](https://github.com/apache/thrift) and [gRPC](https://github.com/grpc/grpc) on
Ubuntu 14.

## Using Thrift

1. Install Thrift as follows (though if you want the latest version of Thrift,
you should build it from source).

  - `sudo pip install thrift`
  - `sudo apt-get install thrift-compiler`
  - `sudo apt-get install ipython`

2. Then do the following (after cloning this repository).

  - `cd rpc-demo/thrift_files`
  - Generate the Python files with

    ```
    thrift --gen py messages.thrift
    ```

3. Run the code.

  - Start the server with `python server.py`.
  - Start the client with `python client.py`. This drops you into an ipython shell.
  - Enter commands in the client such as

    ```
    client.SayHello("Robert")
    ```
    to send a message to the server process. Or
    ```
    %timeit client.SayHello("Robert")
    ```
    to benchmark the rpc.

## Using gRPC

1. Install gRPC with the commands below.

  - `sudo pip install grpcio`
  - `sudo apt-get install build-essential autoconf libtool`
  - `sudo apt-get install ipython`
  - `git clone https://github.com/grpc/grpc.git`
  - `cd grpc`
  - `git submodule update --init`
  - `make`
  - `sudo make install`
  - `sudo apt-get install protobuf-compiler` (to keep setup simple, we use an old version of Protobuf)

2. After that, do the following (after cloning this repository).

  - `cd rpc-demo/grpc_files`
  - Generate the Python files with

    ```
    protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` messages.proto
    ```

3. Run the code.

  - Start the server with `python server.py`
  - Start the client with `python client.py`
  - Enter commands such as

    ```
    stub.SayHello(messages_pb2.HelloRequest(name="Robert"), 1)
    ```
    to send a message to the server process. Or
    ```
    %timeit stub.SayHello(messages_pb2.HelloRequest(name="Robert"), 1)
    ```
