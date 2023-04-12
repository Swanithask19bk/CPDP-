import socket
from _thread import *
import sys

# Server and Port Details
server = "10.136.226.70"  # replace this with you local IP address.
port = 5555

# Creating Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind Socket
try:
    sock.bind((server,port))

except socket.error as socket_error:
    str(socket_error)

# listening for connections
sock.listen(2)
print( "Connecting to Server")

# Sample code for player
def player_client(connections):
   connections.send(str.encode(" connected"))
   reply = ""
   while True:
       try:
           data = connections.recv(2048)  # increase this size if needed to send more information
           reply = data.decode("utf-8")

           if not data:
               print("disconnected from client")
               break
           else:
               print("Recevied:", reply)
               print("sending", reply)
           connections.sendall(str.encode(reply))

       except:
           break

   print("Lost connection")
   connections.close()


while True:
    connections, address_client = sock.accept()
    print("Connected to ", address_client)
    start_new_thread(player_client, (connections,))