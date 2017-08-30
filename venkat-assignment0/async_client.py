import zmq
import sys
import threading
import time
from random import randint, random

def tprint(msg):
    """like print  , but won't get newlines confused with multiple threads"""
    sys.stdout.write(msg + '\n')
    sys.stdout.flush()

class ClientTask(threading.Thread):
    """ClientTask"""
    def __init__(self, id):
        self.id = id
        threading.Thread.__init__ (self)

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
	identity = u'worker-%d' % self.id
        socket.identity = identity.encode('ascii')
        socket.connect('tcp://localhost:5570')
        print('Client %s started' % (identity))
        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)
	socket.send_string("Blah")
	for i in range(5):
		sockets = dict(poll.poll(1000))
		if socket in sockets:
			msg = socket.recv()
                	tprint('Client %s received: %s' % (identity, msg))

	socket.close()
        context.term()

def main():
	client = ClientTask(0)
	client.start()

if __name__ == "__main__":
	main()
