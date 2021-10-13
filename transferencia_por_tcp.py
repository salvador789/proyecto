import os, argparse, socket, socketserver, binascii

class tcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        datos = self.request.recv(512).strip()
        if datos.startswith(b"send:"):
            arch = datos.split(b":")[1] # en la variable arch manejamos una lista
                                        # esta lista tiene 2 elementos la info, y el nombre
            print("Reciviendo archivo:" +arch.decode())
            with open(str(arch.decode("utf-8")), "wb") as f:
                while datos:
                    datos = bytearray(self.request.recv(512).strip())
                    if len(datos) % 2 == 0:
                        f.write(binascii.unhexlify(datos))
                    else:
                        f.write(binascii.unhexlify(datos.append(0)))
        print("Archivo recivido....")

def iniciarServer(args):
    servidor = socketserver.TCPServer(("", args.puerto), tcpServer)
    print("[Servidor en linea!!!!]")
    servidor.serve_forever()

def iniciarCliente(args):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((args.ip, args.puerto))
        path, arch = os.path.split(args.archivo)
        print("Enviando Archivo!!!" + args.archivo)
        s.sendall(b"send:" + bytes(arch,))
        with open(args.archivo, 'rb') as a:
            datos = a.read(512)
            while(datos):
                s.sendall(binascii.hexlify(datos))
                datos = a.read(512)
        s.close()
        print("Archivo enviado:"+ args.archivo)

def main(args):
    if (args.cliente):
        iniciarCliente(args)
    elif (args.servidor):
        iniciarServer(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cliente", action="store", help="Iniciar cliente", type=str, nargs='?', default=False, const=True)
    parser.add_argument("-s", "--servidor", action="store", help="Iniciar servidor", type=str, nargs='?', default=False, const=True)
    parser.add_argument("-i", "--ip", action="store", help="Ip del servidor", type=str)
    parser.add_argument("-p", "--puerto", action="store", help="Puerto del servidor", type=int)
    parser.add_argument("-a", "--archivo", action="store", help="Archivo que se enviara", type=str)

    args = parser.parse_args()
    if (not args.cliente and not args.servidor):
        parser.print_help()
        print("\n debes poner si vas a usar --cliente o --servidor")
        parser.exit()
    main(args)

