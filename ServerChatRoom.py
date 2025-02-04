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
    #infinite listening
    while True:
        #accept incoming connections
        client_socket, address = server_socket.accept()
        print(f"Connected with{address} ..")
        #get the name of the client getting connected
        client_socket.send("NAME".encode("utf-8"))
        client_name = client_socket.recv(SIZE_OF_BYTES).decode('utf-8')
        #append to list
        CLIENT_NAME.append(client_name)
        CLIENT_SOCKET_LIST.append(client_socket)
        #update the server, and all clients
        print(f"Name of new client is {client_name}\n")
        client_socket.send(f"{client_name} you connected to server".encode('utf-8'))
        broadcast_message(f"{client_name} joined the server".encode("utf-8"))

#connect client
connect_client()

