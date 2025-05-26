from socket import *
import sys

srvPort = 8080
srvSocket = socket(AF_INET, SOCK_STREAM)
srvAddress = ('localhost', srvPort)
srvSocket.bind(srvAddress)



