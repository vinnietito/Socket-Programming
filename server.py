import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 8080 # Reserve a port for your service

# Bind the socket to the port
server_socket.bind((host, port))

# Put the socket into listening mode
server_socket.listen(5)
print(f"Server is listening on {host}:{port}...")

while True:
    # Establish a connection with the client
    client_socket, addr = server_socket.accept()
    print