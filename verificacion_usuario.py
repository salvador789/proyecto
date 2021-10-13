#!/usr/bin/python3.8

import argparse

parser = argparse.ArgumentParser(description='Verificar usuarios')
parser.add_argument('nombre_del_usuario')
args = parser.parse_args()

if args.nombre_del_usuario == 'Admin':
 print("Hola admin")
elif args.nombre_del_usuario == 'admin':
 print("Hola admin")
 
else:
 print("Hola usuario normal")

