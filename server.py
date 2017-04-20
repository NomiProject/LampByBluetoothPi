#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import bluetooth as bt
import RPi.GPIO as GPIO

RaspberryPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RaspberryPin, GPIO.OUT)

server_socket= bt.BluetoothSocket(bt.RFCOMM)

server_socket.bind(("", 3))
server_socket.listen(1)

while True:
    try:
        client_socket, client_info = server_socket.accept()
        data = client_socket.recv(1024)
        if data == "on":
            GPIO.output(RaspberryPin, True)
            print("Ativando pino %d" % RaspberryPin)
        elif data == "off":
            GPIO.output(RaspberryPin, False)
            print("Desativando pino %d" % RaspberryPin)
        else:
            break
        client_socket.close()
    except IOError:
        break
    
print("Serviço Encerrado")
server_socket.close()