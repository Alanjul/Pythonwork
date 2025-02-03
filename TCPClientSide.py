
#import packages for TCP client side
import socket
#create a client side with IPv4 and TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the socket to the server
ip_address = socket.gethostbyname(socket.gethostname())
client_socket.connect((ip_address, 12345))
#receive the message from the server with recv with maximum numbe of bits
message = client_socket.recv(1024)
print(message.decode("utf-8"))
print(type(message))
client_socket.close()