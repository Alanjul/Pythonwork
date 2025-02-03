import socket
#create server socket using AFI_NET and UDP (SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind our new socket to a tuple (ip address, port address) as a tuple
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12641))

#we are not listening or accepting connections since UDP is connectionless protocol
message, address = server_socket.recvfrom(1024)
print(message.decode('utf-8'))
print(address)
server_socket.close()

