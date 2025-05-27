from socket import *
from utilities import *
import mimetypes as mt # Permits to manage the content type

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

            # It determines the MIME type of the file based on its extension
            mime_type = get_mime_type(str(filename[1:].decode('utf-8')))
            print("MIME type determined: ", mime_type)

            # To send a binary file (eg.img), distinguish between text and binary files
            if mime_type.startswith('text/'):
                f = open(filename[1:], 'r')
                outputdata = f.read()
                print_and_log("Text data sent to the client:")
                print_and_log(outputdata)
                f.close()

                # Send HTTP header with OK response
                connectionSocket.send(("HTTP/1.1 200 OK\r\nContent-Type: " + mime_type + "\r\n\r\n").encode())
                connectionSocket.send(outputdata.encode('utf-8'))
            else:
                f = open(filename[1:], 'rb')
                outputdata = f.read()
                print_and_log("Binary data sent to the client.")
                f.close()

                # Send HTTP header with OK response
                connectionSocket.send(("HTTP/1.1 200 OK\r\nContent-Type: " + mime_type + "\r\n\r\n").encode())
                connectionSocket.send(outputdata) # Send binary data directly
            connectionSocket.send("\r\n".encode())
    except IOError:
        # Send response message for file not found
        print_and_log('File not found, sending 404 response...')
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send(notFoundPage.encode())
    print_and_log('Response sent successfully. Connection closed.')
    connectionSocket.close()






