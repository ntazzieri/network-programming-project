from socket import *
from utilities import *
import sys

srvPort = 8080
srvSocket = socket(AF_INET, SOCK_STREAM)
srvAddress = ('localhost', srvPort)
srvSocket.bind(srvAddress)


srvSocket.listen(1)
print_and_log('=' * 50)
print_and_log('Welcome')
print_and_log('The web server is ready to receive connections on port:' + str(srvPort))

notFoundPage = get_404_page()

while True:
    print_and_log('waiting for a connection...')
    connectionSocket, addr = srvSocket.accept()
    print_and_log('Connection established with:'+ str(addr))
    print_and_log('Connection socket:'+ str(connectionSocket))
    try:
        message = connectionSocket.recv(1024)
        if len(message.split()) > 0:
            print_and_log(str(message) + '::' + str(message.split()[0]) + ':' + str(message.split()[1]))
            filename = message.split()[1]
            print_and_log(str(filename) + '||' + str(filename[1:]))
            f = open(filename[1:], 'r')
            outputdata = f.read()
            print_and_log(outputdata)
            f.close()

            # Send HTTP header with OK response
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.send(outputdata.encode())
            connectionSocket.send("\r\n".encode())
    except IOError:
        # Send response message for file not found
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes(notFoundPage, "UTF-8"))
    print_and_log('Response sent successfully. Connection closed.')
    connectionSocket.close()






