#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import argparse
import bluetooth as bt


cli = argparse.ArgumentParser()
cli.add_argument("-s", "--send", type=str, help="Send 'on', 'off' or 'exit'")
options = vars(cli.parse_args())

#print("Procurando RaspberryPI...")
rasbBluetoothName = "raspberrypi"
raspBluetoothMac = "B8:27:EB:76:C1:C3"

'''
for addr, name in bt.discover_devices(lookup_names=True):
    if name == rasbBluetoothName:
        raspBluetoothMac = addr
        break

if raspBluetoothMac is None:
    print("Não foi possível localizar nenhum Raspberry!")
    exit()
'''

#print("Conectado com sucesso ao endereço %s" % raspBluetoothMac)
    
client_socket = bt.BluetoothSocket(bt.RFCOMM)
client_socket.connect((raspBluetoothMac, 3))
client_socket.send(options["send"])

if options["send"] != "on" or "off":
    print("Desligando servidor Bluetooth!")

#print ("Opção [%s] enviada com sucesso!" % options["send"])

client_socket.close()
    
