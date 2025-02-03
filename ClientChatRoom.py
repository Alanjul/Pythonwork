#client side
import socket, threading
#constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 4521
BYTE_SIZE = 2048

#create socket
client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_PORT,DEST_IP)) #connected as tuple with dest port and ipp
def send_message():
    """The client sends the message to the server"""
    pass
def receive_message():
    """Receive message from the server"""
    pass