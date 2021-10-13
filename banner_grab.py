import sys, argparse, socket, multiprocessing, subprocess, time
from datetime import datetime


def escaneo(ip, puerto):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        respuesta = s.connect_ex((ip, puerto))
        if respuesta == 0:
            if puerto == 80:
                rsp = "HEAD / HTTP/1.1\r\nhost:  " + "\r\n\r\n"
                s.send(rsp.encode())
            banner = s.recv(4096)
            mensaje = "[*] Puerto " + str(puerto) + " Abierto\n"
            mensaje += "================================\n" + banner.strip().decode()
            print(mensaje + "\n====================================\n")
        s.close()
    except socket.timeout:
        banner = "No es posible conectar"


def main(args):
    try:
        args.throttle = float(args.throttle)
        start = datetime.now()
        print("\n========================================\n")
        print("Escaneando: " + args.ip + " Puertos: " + str(args.puerto_i) + '...' + str(args.puerto_f))
        print("\n========================================\n")
        puertos = range(args.puerto_i, args.puerto_f+1)
        for puerto in puertos:
            p = multiprocessing.Process(target=escaneo, args=(args.ip, puerto,))
            p.start()
            time.sleep(args.throttle)
        time.sleep(2)
        end = datetime.now()
        print("\n========================================\n")
        print("El escaneo duro: " + str(end - start))
        print("\n========================================\n")
    except Exception as error:
        print(str(error))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", action="store", help="Ip a escanear", type=str)
    parser.add_argument("puerto_i", action="store",  help="Puerto de inicio", type=int)
    parser.add_argument("puerto_f", action="store",  help="Puerto final", type=int)
    parser.add_argument("-t", "--throttle", action="store", help="Acelerador", nargs="?", default=0.25, const=0.05)

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()
    main(args)
