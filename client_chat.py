#import packages
import socket
#constants
DESTINATION_IP = socket.gethostbyname(socket.gethostname())
ENCODER = 'utf-8'
DEST_PORT = 45215
BYTESIZE = 1024

#create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the server
client_socket.connect((DESTINATION_IP, DEST_PORT))
while True:
    #receive the message from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    if message == 'quit':
        #client sends the messages to the server to quit
        client_socket.send("quit".encode(ENCODER))
        print("\nWe are ending the connection now .......")
        #break out of the loop
        break
    else:
        print(f"\n{message}")
        #send some message to the server
        message = input("Message:")
        client_socket.send(message.encode(ENCODER))
#close the client socket
client_socket.close()