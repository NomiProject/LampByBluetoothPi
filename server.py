#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import bluetooth as bt

server_socket= bt.BluetoothSocket(bt.RFCOMM)

server_socket.bind(("", 3))
server_socket.listen(1)

client_socket, client_info = server_socket.accept()

try:
    while True:
        data = client_socket.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
except IOError:
    pass

client_socket.close()
server_socket.close()