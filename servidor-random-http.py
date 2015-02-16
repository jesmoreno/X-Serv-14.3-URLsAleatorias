#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
        while True:
                print 'Waiting for connections'
                (recvSocket, address) = mySocket.accept()
                print 'Request received:'
                print recvSocket.recv(2048)
                print 'Answering back...'
                numeroAleatorio = str(random.randrange(1000000))
                recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body><h1>URL'S ALEATORIAS</h1>" +
                                "<p>Hola.<A HREF='"+ numeroAleatorio + "'>Dame otra</A></p>" +
                                "</body></html>" + "\r\n")
                recvSocket.close()
except KeyboardInterrupt:
        print "Closing binded socket"
        mySocket.close()
