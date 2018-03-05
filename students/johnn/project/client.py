
import zmq

# Prepare our context and sockets
context = zmq.Context()

me = context.socket(zmq.REQ)
me.connect("tcp://127.0.0.1:5561")

# Process messages from both sockets
message = "hello world"
me.send_string(message)
print("sent:", message)
in_message = me.recv_string()
print("got back:", str(in_message))
