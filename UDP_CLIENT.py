#udp client side
import socket
#create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#send some imformation to the connectionless protocol
client_socket.sendto("hello server i am want connection". encode('utf-8'),(
                     socket.gethostbyname(socket.gethostname()), 12641))