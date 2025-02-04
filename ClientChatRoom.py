#client side
import socket, threading
#constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 35412
BYTE_SIZE = 2048

#create socket
client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT)) #connected as tuple with dest port and ipp
def send_message():
    """The client sends the message to the server"""
    pass
def receive_message():
    """Receive message from the server"""
    while True:
        """use try and except to receive the message from server"""
        try:
            message = client_socket.recv(BYTE_SIZE).decode("utf-8")
            #check for flag name
            if message == "NAME":
                name = input("Enter name: ")
                client_socket.send(name.encode('utf-8'))
            else:
                print(message)
        except :
            #error
            print("an error occured")
            client_socket.close()
            break
#start chart
receive_message()