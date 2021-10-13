import socket

equipo = '192.168.1.82'
puerto = 31337


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 s.bind((equipo, puerto))
 s.listen()
 conexion, direccion = s.accept()
 with conexion:
     print("Un cliente con la direcion ip: "+str(direccion) + "se ha conectado")
     while True:
         datos = conexion.recv(1024)
         if not datos:
             break
         else:
             conexion.sendall(datos)