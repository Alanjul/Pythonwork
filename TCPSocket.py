
#import packages for TCP serverSide
import socket
#create a server side socket using IPV4(AF_INET)
#and TCP with SOCK_STREAM
server_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Getting Host name")
print(socket.gethostname)
#listen for incoming connections
#getting the ip dynamically
ip_address = socket.gethostbyname(socket.gethostname())
print(ip_address)
#getting the port number
server_socket.bind((ip_address, 12345))
server_socket.listen() #listen for incoming connections
#listen continously
while True:
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print("The Client side\n")
    print(client_socket)
    print("Client address \n")
    print(client_address)

    print(f"Connected to {client_address}")

    #call the client socket
    client_socket.send("Your are connected".encode("utf-8"))
    #close the connection
    server_socket.close()
