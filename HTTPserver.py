from socket import *
from utilities import *
import sys

srvPort = 8080
srvSocket = socket(AF_INET, SOCK_STREAM)
srvAddress = ('localhost', srvPort)
srvSocket.bind(srvAddress)


srvSocket.listen(1)
print('The web server is ready to receive connections on port:', srvPort)

notFoundPage = get_404_page()

while True:
    print('waiting for a connection...')
    connectionSocket, addr = srvSocket.accept()
    print('Connection established with:', addr)
    print('Connection socket:', connectionSocket)
    try:
        message = connectionSocket.recv(1024)
        if len(message.split()) > 0:
            print(message, '::', message.split()[0], ':', message.split()[1])
            filename = message.split()[1]
            print(filename, '||', filename[1:])
            f = open(filename[1:], 'r')
            outputdata = f.read()
            print(outputdata)
            f.close()

            # Send HTTP header with OK response
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.send(outputdata.encode())
            connectionSocket.send("\r\n".encode())
    except IOError:
        # Send response message for file not found
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes(notFoundPage, "UTF-8"))
    print('Response sent successfully. Connection closed.')
    connectionSocket.close()






