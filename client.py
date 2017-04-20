#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com


import bluetooth as bt

print("Procurando RaspberryPI...")
rasbBluetoothName = "raspberrypi"
raspBluetoothMac = None


for addr, name in bt.discover_devices(lookup_names=True):
    if name == rasbBluetoothName:
        raspBluetoothMac = addr
        break

if raspBluetoothMac is None:
    print("Não foi possível localizar nenhum Raspberry!")
    exit()

print("Raspberry MAC %s" % raspBluetoothMac)
    

client_socket = bt.BluetoothSocket(bt.RFCOMM)
client_socket.connect((raspBluetoothMac, 3))
client_socket.send("Hello World")

print ("Finished")

client_socket.close()
    
