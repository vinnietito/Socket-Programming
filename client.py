import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server address
host = socket.gethostname()  # Use '127.0.0.1' for localhost
port = 8080  # Same port as the server

# Connect to the server
client_socket.connect((host, port))

# Send a message to the server
message = "Hello, server!"
client_socket.send(message.encode())

# Receive a response from the server
response = client_socket.recv(1024).decode()
print(f"Received response from server: {response}")

# Close the connection
client_socket.close()
