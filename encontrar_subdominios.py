#!/usr/bin/python3.8
import requests
from threading import Thread
from queue import Queue

q = Queue()

def obtener_subdominio(dominio):
    global q
    while True:
        subdominio = q.get()
        url = f"https://{subdominio}.{dominio}"
        try:
            requests.get(url,)
        except requests.ConnectionError:
            pass
        else:
            print("[+] se encontro el siguiente subdominio: ", url)
        q.task_done()

def main(dominio, n_trheads, subdominio):
    global q
    for subdom in subdominio:
        q.put(subdom)

    for t in range(n_trheads):
        hilo = Thread(target=obtener_subdominio, args=(dominio,))
        hilo.daemon = True
        hilo.start()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Obtener subdomionos con uso de threads para mas velocidad')
    parser.add_argument("dominio", help="Dominio a escanear en busca de subminios. No es necesario poner http o https")
    parser.add_argument("-l", "--lista", help="Diccionario de subdominios", default='subdominios.txt')
    parser.add_argument("-t", "--num_hilos", help="Numero de hilos a usar en este srcipt, por defualt son 10", default=10, type=int)

    args = parser.parse_args()
    dominio = args.dominio
    lista = args.lista
    num_hilos = args.num_hilos

main(dominio=dominio, n_trheads=num_hilos, subdominio=open(lista).read().splitlines())
q.join()

