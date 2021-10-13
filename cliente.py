import socket

equipo= "192.168.1.82"
puerto= 31337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((equipo, puerto))
    s.sendall(b"Hola, soy estudiante del curso black hat hacking con python 3!")
    datos = s.recv(1024)

    print("Respuesta recivida" + repr(datos.decode()))
