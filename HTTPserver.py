from socket import *
from utilities import *

srvPort = 8080
srvSocket = socket(AF_INET, SOCK_STREAM)
srvAddress = ('localhost', srvPort)
srvSocket.bind(srvAddress)

# backlog queue length set to 1
srvSocket.listen(1)
print_and_log('=' * 50)
print_and_log('Welcome')
print_and_log('The web server is ready to receive connections on port:' + str(srvPort))

while True:
    print_and_log('waiting for a connection...')
    connection_socket, addr = srvSocket.accept()
    print_and_log('Connection established with:'+ str(addr))
    print_and_log('Connection socket:'+ str(connection_socket))
    try:
        message = connection_socket.recv(1024)
        if len(message.split()) > 0:
            filename = message.split()[1].decode('utf-8')
            print_and_log('Requested file: ' + str(filename))

            # It determines the MIME type of the file based on its extension
            mime_type = get_mime_type(str(filename[1:]))
            print("MIME type determined: ", mime_type)

            # Distinguish between text and binary files
            if mime_type.startswith('text/'):
                f = open(filename[1:], 'r')
                file_content = f.read()
                print_and_log("Text data sent to the client.")
                # print_and_log(file_content) # Uncomment this line to log the content of the file that is sent to the client
                f.close()

                # Send HTTP header with OK response
                connection_socket.send(("HTTP/1.1 200 OK\r\nContent-Type: " + mime_type + "\r\n\r\n").encode())
                connection_socket.send(file_content.encode('utf-8'))
            else:
                f = open(filename[1:], 'rb')
                file_content = f.read()
                print_and_log("Binary data sent to the client.")
                f.close()

                # Send HTTP header with OK response
                connection_socket.send(("HTTP/1.1 200 OK\r\nContent-Type: " + mime_type + "\r\n\r\n").encode())
                connection_socket.send(file_content) # Send binary data directly
            connection_socket.send("\r\n".encode())
    except IOError:
        # Send response message for file not found
        print_and_log('File not found, sending 404 response...')
        connection_socket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connection_socket.send(get_404_page().encode())
    print_and_log('Response sent successfully. Connection closed.')
    connection_socket.close()






