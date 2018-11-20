#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

try:
# Dirección IP del servidor.
    METHOD = sys.argv[1]
    SERVER = sys.argv[2]
    SERVER_NUMBER_ = SERVER.split('@')[1]
    SERVER_NAME = SERVER.split('@')[0]
    SERVER_NUMBER = SERVER_NUMBER_.split(':')[0]
    PORT = int(SERVER_NUMBER_.split(':')[1])
except (ValueError, IndexError):
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Contenido que vamos a enviar
LINE = (METHOD + ' sip:' + SERVER_NAME + '@' + SERVER_NUMBER + ' SIP/2.0')

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER_NUMBER, PORT))

    print("Enviando: ")
    print(LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print("\n")
    print('Recibiendo: ')
    print(data.decode('utf-8'))

    server_text = data.decode('utf-8').split(' ')
    if server_text[1] == '100':
        line_ack = ('ACK sip: ' + SERVER_NAME + '@' + SERVER_NUMBER
                    + ' SIP/2.0')
        my_socket.send(bytes(line_ack, 'utf-8') + b'\r\n')

        data = my_socket.recv(1024)
