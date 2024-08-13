import socket

print("Client.py has started running")

localIP, localPort = "10.0.0.49", 65432

TCPclientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPclientSocket.connect((localIP,localPort))

clientMessage = input("Type your message for the server here: ")
data = bytes(clientMessage, "utf-8")

# send the message to the server using TCP socket
print("Sending message to {0} port {1}".format(localIP,localPort))
TCPclientSocket.sendall(data)

# receiving reply from the server
dataFromServer = str(TCPclientSocket.recv(1024))
print("Message received from the server: ", str(dataFromServer))
