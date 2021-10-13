#!/usr/bin/python3.8

import socket
import subprocess
import sys

subprocess.call('clear', shell=True)

objetivo = raw_input("Ingresa la direccion ip o el nombre del equipo o la pagina web: ")
ip_objetivo = socket.gethostbyname(objetivo)

print("=" * 50)
print("Escaneando: ", objetivo)
print("=" * 50)

t1 = datetime.now()

try:
 for puerto in range(1,1024):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  resultado - s.connect_ex((objetivo, puerto))
  if resultado == 0:
   print("Puerto {}: Abierto".format(puerto))
 s.close()

except KeyboardInterrupt:
 print("Presionaste CTRL+C")
 sys.exit()

except socket.gainerror:
 print("No se puede establercer conexion con el objetivo")
 sys.exit()

t2 = datetime.now()
total = t2 - t1

print("Escaneo completado en: ",total)

