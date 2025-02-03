import socket

#define constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_ADDRESS = 45215
ENCODER = 'utf-8'
BIT_SIZE = 1024
#create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_ADDRESS))
#listen for connection
server_socket.listen()
#accept incoming connections
print("Server is running ----\n")
client_socket, client_address = server_socket.accept()
client_socket.send("you are now connect to the server".encode(ENCODER))

#send and receive the message from the client
while True:
    #receive the message from the client
    message = client_socket.recv(BIT_SIZE).decode(ENCODER)
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("The chat is ending now, Thank you")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))
#close the server if the  everything is done
server_socket.close()
