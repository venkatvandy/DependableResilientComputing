Run the following commands on two different terminals in the following order:
1. python async_server.c
2. python async_client.c

You will see that the server sends back to the client twice what the client sends it.

Since the requirement is that the client must receive back two messages back from the server, we cannot use a simple REQ-REPLY ZMQ socket.
So, I have used asynchronous Req-Reply ZMQ sockets for communication.
The way it works is 
1. Client connects to server and sends request 
2. The server acts as a router and creates workers for itself to handle requests from clients. So it can send 0 or more messages back to the client.

The client can receive multiple messages from the server without having to block.
