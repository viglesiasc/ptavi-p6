#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

IP = sys.argv[1]
PORT = int(sys.argv[2])
AUDIO_FILE = (sys.argv[3])


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):

        line = self.rfile.read()
        client_method = line.decode('utf-8').split(' ')[0]
        print("El cliente nos manda: ")
        print(line.decode('utf-8'))

        if client_method == 'INVITE':
            self.wfile.write(b"SIP/2.0 100 Trying\n")
            self.wfile.write(b"SIP/2.0 180 Ringing\n")
            self.wfile.write(b"SIP/2.0 200 OK\n")
        elif client_method == 'ACK':
            self.wfile.write(b"SIP/2.0 200 OK\n")
        elif client_method == 'BYE':
            self.wfile.write(b"SIP/2.0 200 OK\n")
        else:
            self.wfile.write(b"SIP/2.0 405 Method Not Allowed\n")

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((IP, PORT), EchoHandler)
    print("Listening...\n")
    serv.serve_forever()
