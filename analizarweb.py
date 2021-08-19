#usr/bin/python3

import os
import time

ruta = os.getcwd()+ "/output"

direccion = input("Digite el sitio web ->")

os.system("whatweb -v -a 3 " + direccion + " > " + ruta + direccion + "whatweb" + ".txt")

os.system("sslscan " + direccion + " > " + ruta + direccion + "_sslscan" + ".txt")

palabra = "WordPress"

f = open(ruta + direccion + _whatweb.txt)
libro = f.read()
n = libro.count(palabra)
f.close()

if n >= 1:
    os.system("wpscan --url " + direccion + " -o " + ruta + direccion + "_wordpress" + ".txt")

    palabra = "Joomla"

    f = open(ruta + direccion + _whatweb.txt)
    libro = f.read()
    n = libro.count(palabra)
    f.close()

if n >= 1:
    os.system("Joomscan --u " + direccion + " -o " + ruta + direccion + "_joomla" + ".txt")
