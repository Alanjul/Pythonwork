#server side chat room
import socket, threading

#constants defined
LOCAL_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 35412
SIZE_OF_BYTES = 2048

#listen for incoming connection'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind them
server_socket.bind((LOCAL_IP,HOST_PORT))
server_socket.listen()

#create lists to store clients and their names
CLIENT_SOCKET_LIST =[]
CLIENT_NAME = []

def broadcast_message(message):
    """send messages to all connected clients"""
    pass
def receive_message(client_socket):
    """receive incoming call"""
    pass
def connect_client():
    """Connect incoming clients"""
    pass
