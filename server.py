import socket

print("Server.py has started running")

ip = "10.0.0.49"
port = 65432

serverAddressPort = (ip, port)

bytesToSend = b'Hey there! We received the message.'

# Creating the TCP/IPv4 Socket
TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding server socket to the port
TCPServerSocket.bind(serverAddressPort)
print("Server is up and listening")


# Listening for incoming messages

TCPServerSocket.listen(10)
message, address = TCPServerSocket.accept()

while 1:
    clientData = message.recv(1024)
    message.sendall(clientData)

